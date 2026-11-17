"""GeneWeaver Day 06 - GPU compatibility checker."""

import platform
import sys
import importlib.util


def check_gpu_environment():
    print("GENEWEAVER - DAY 06 GPU CHECK")
    print("Python:", sys.version.split()[0])
    print("Operating System:", platform.system())

    if importlib.util.find_spec("numba") is None:
        print("Numba: Not installed")
        print("GPU Status: Not configured")
        return False

    try:
        from numba import cuda

        available = cuda.is_available()
        print("Numba CUDA Available:", available)

        if available:
            print("GPU:", cuda.get_current_device().name)
        else:
            print("GPU acceleration unavailable.")
            print("CPU development can continue.")

        return available

    except Exception as error:
        print("CUDA check failed:", error)
        return False


if __name__ == "__main__":
    check_gpu_environment()
