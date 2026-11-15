import sys
from pathlib import Path
from time import perf_counter

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from alignment import count_mismatches


def benchmark_alignment(genome_size):
    """Measure CPU alignment performance."""
    target = "ATGCGTAC"
    genome = "ATGC" * (genome_size // 4)

    start = perf_counter()
    matches = 0

    for i in range(len(genome) - len(target) + 1):
        segment = genome[i:i + len(target)]

        if count_mismatches(segment, target) <= 2:
            matches += 1

    elapsed = perf_counter() - start

    return matches, elapsed


if __name__ == "__main__":
    print("GENEWEAVER - DAY 05 CPU BENCHMARK")

    for size in [1000, 10000, 100000]:
        matches, elapsed = benchmark_alignment(size)

        print(f"Genome Size: {size}")
        print(f"Matches Found: {matches}")
        print(f"Execution Time: {elapsed:.6f} seconds")
        print("-" * 35)
