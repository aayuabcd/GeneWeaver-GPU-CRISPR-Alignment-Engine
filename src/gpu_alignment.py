"""GeneWeaver Day 07 - CUDA DNA alignment kernel."""

import numpy as np
from numba import cuda


@cuda.jit
def dna_alignment_kernel(genome, target, results):
    """Calculate mismatches for each possible target position."""
    idx = cuda.grid(1)

    if idx < results.size:
        mismatches = 0

        for j in range(target.size):
            if genome[idx + j] != target[j]:
                mismatches += 1

        results[idx] = mismatches


def cpu_alignment(genome, target):
    """Reference CPU implementation."""
    if len(target) == 0 or len(target) > len(genome):
        raise ValueError("Invalid target length")

    return [
        sum(a != b for a, b in zip(
            genome[i:i + len(target)], target
        ))
        for i in range(len(genome) - len(target) + 1)
    ]


def gpu_alignment(genome, target):
    """Execute the alignment kernel on a CUDA GPU."""
    if not cuda.is_available():
        raise RuntimeError("CUDA GPU is not available")

    if len(target) == 0 or len(target) > len(genome):
        raise ValueError("Invalid target length")

    genome_array = np.frombuffer(genome.encode("ascii"), dtype=np.uint8)
    target_array = np.frombuffer(target.encode("ascii"), dtype=np.uint8)

    result_size = len(genome) - len(target) + 1
    results = np.zeros(result_size, dtype=np.int32)

    d_genome = cuda.to_device(genome_array)
    d_target = cuda.to_device(target_array)
    d_results = cuda.to_device(results)

    threads_per_block = 128
    blocks = (result_size + threads_per_block - 1) // threads_per_block

    dna_alignment_kernel[blocks, threads_per_block](
        d_genome, d_target, d_results
    )

    return d_results.copy_to_host().tolist()


if __name__ == "__main__":
    genome = "ATGCGTACATGAGTAC"
    target = "ATGCGTAC"

    print("GENEWEAVER - DAY 07 GPU ALIGNMENT")

    results = cpu_alignment(genome, target)
    print("CPU mismatch results:", results)

    if cuda.is_available():
        print("GPU mismatch results:", gpu_alignment(genome, target))
    else:
        print("CUDA unavailable: GPU execution requires compatible hardware.")
