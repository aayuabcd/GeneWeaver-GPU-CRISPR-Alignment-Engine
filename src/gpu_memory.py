"""GeneWeaver Day 08 - CPU/GPU memory transfer utilities."""

from time import perf_counter

import numpy as np
from numba import cuda


def prepare_transfer_data(data):
    """Convert input data into a one-dimensional NumPy array."""
    array = np.asarray(data, dtype=np.int32)

    if array.ndim != 1 or array.size == 0:
        raise ValueError("Input must be a non-empty one-dimensional array")

    return array


def transfer_to_gpu(data):
    """Transfer prepared data from CPU memory to GPU memory."""
    if not cuda.is_available():
        raise RuntimeError("CUDA GPU is not available")

    array = prepare_transfer_data(data)

    start = perf_counter()
    device_array = cuda.to_device(array)
    elapsed = perf_counter() - start

    return device_array, elapsed


def retrieve_from_gpu(device_array):
    """Copy results from GPU memory back to CPU memory."""
    if not cuda.is_available():
        raise RuntimeError("CUDA GPU is not available")

    start = perf_counter()
    result = device_array.copy_to_host()
    elapsed = perf_counter() - start

    return result, elapsed


if __name__ == "__main__":
    print("GENEWEAVER - DAY 08 MEMORY TRANSFERS")

    sample_data = [0, 1, 2, 3, 4]
    cpu_data = prepare_transfer_data(sample_data)

    print("CPU data:", cpu_data)

    if cuda.is_available():
        device_data, upload_time = transfer_to_gpu(cpu_data)
        result, download_time = retrieve_from_gpu(device_data)

        print("GPU-to-CPU result:", result)
        print(f"CPU-to-GPU time: {upload_time:.6f} seconds")
        print(f"GPU-to-CPU time: {download_time:.6f} seconds")
    else:
        print("CUDA unavailable: actual GPU transfers were not executed.")
