import pytest

from src.gpu_alignment import cpu_alignment


def test_exact_match():
    assert cpu_alignment("ATGC", "ATGC") == [0]


def test_multiple_positions():
    assert cpu_alignment("ATGCATGC", "ATGC") == [0, 4, 0, 4, 0]


def test_mismatch():
    assert cpu_alignment("ATGT", "ATGC") == [1]


def test_invalid_target():
    with pytest.raises(ValueError):
        cpu_alignment("ATGC", "")


def test_target_longer_than_genome():
    with pytest.raises(ValueError):
        cpu_alignment("AT", "ATGC")
