# 3. Context manager de temporización
# with, context managers
import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.perf_counter()

    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"Tiempo transcurrido: {elapsed:.4f} segundos")
