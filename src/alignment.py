def count_mismatches(sequence, target):
    if len(sequence) != len(target):
        raise ValueError("Sequences must have equal length")

    return sum(a != b for a, b in zip(sequence, target))


if __name__ == "__main__":
    dna = "ATGCGTAC"
    target = "ATGAGTAC"

    print("GeneWeaver CPU Alignment")
    print("Mismatches:", count_mismatches(dna, target))
