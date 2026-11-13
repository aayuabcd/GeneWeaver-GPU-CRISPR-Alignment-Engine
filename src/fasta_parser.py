from pathlib import Path


def parse_fasta(file_path):
    """Read DNA sequences from a FASTA file."""
    sequences = {}
    name = None
    parts = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if name is not None:
                    sequences[name] = "".join(parts)

                name = line[1:].strip()
                parts = []
            elif name is None:
                raise ValueError("Invalid FASTA format")
            else:
                parts.append(line.upper())

    if name is not None:
        sequences[name] = "".join(parts)

    return sequences


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "data" / "sample_genome.fasta"

    for name, sequence in parse_fasta(path).items():
        print("Sequence:", name)
        print("DNA:", sequence)
        print("Length:", len(sequence))
