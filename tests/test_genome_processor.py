from src.genome_processor import validate_dna, chunk_genome


def test_valid_dna():
    assert validate_dna("atgc") == "ATGC"


def test_genome_chunking():
    assert chunk_genome("ATGCGTAC", 4) == ["ATGC", "GTAC"]


def test_invalid_dna():
    import pytest

    with pytest.raises(ValueError):
        validate_dna("ATGX")
