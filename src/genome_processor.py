def validate_dna(sequence):
    """Validate a DNA sequence."""
    sequence = sequence.upper().strip()

    if not sequence:
        raise ValueError("DNA sequence cannot be empty")

    if any(base not in "ACGT" for base in sequence):
        raise ValueError("Invalid DNA sequence")

    return sequence


def chunk_genome(sequence, chunk_size=1000):
    """Split DNA into smaller chunks."""
    sequence = validate_dna(sequence)

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    return [
        sequence[i:i + chunk_size]
        for i in range(0, len(sequence), chunk_size)
    ]


if __name__ == "__main__":
    genome = "ATGCGTACATGAGTACATGCGTTC"

    chunks = chunk_genome(genome, 8)

    print("GeneWeaver - Day 04")
    print("Genome length:", len(genome))
    print("Total chunks:", len(chunks))

    for index, chunk in enumerate(chunks, 1):
        print(f"Chunk {index}: {chunk}")
