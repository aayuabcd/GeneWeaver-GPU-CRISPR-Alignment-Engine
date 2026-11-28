import numpy as np
import pytest
from numba import cuda

from src.gpu_memory import (
    prepare_transfer_data,
    transfer_to_gpu,
    retrieve_from_gpu,
)


def test_prepare_transfer_data():
    result = prepare_transfer_data([1, 2, 3])
    assert np.array_equal(result, np.array([1, 2, 3], dtype=np.int32))


def test_prepare_rejects_empty_data():
    with pytest.raises(ValueError):
        prepare_transfer_data([])


def test_prepare_rejects_multidimensional_data():
    with pytest.raises(ValueError):
        prepare_transfer_data([[1, 2], [3, 4]])


def test_gpu_memory_transfer():
    if not cuda.is_available():
        pytest.skip("CUDA GPU unavailable")

    device_data, upload_time = transfer_to_gpu([1, 2, 3])
    result, download_time = retrieve_from_gpu(device_data)

    assert np.array_equal(result, [1, 2, 3])
    assert upload_time >= 0
    assert download_time >= 0


def test_transfer_reports_unavailable_cuda():
    if cuda.is_available():
        pytest.skip("CUDA is available; unavailable-GPU test not applicable")

    with pytest.raises(RuntimeError, match="CUDA GPU is not available"):
        transfer_to_gpu([1, 2, 3])
