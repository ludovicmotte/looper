from contextlib import contextmanager
import time


@contextmanager
def log_duration(name="Bloc"):
    start = time.time()
    yield
    duration = time.time() - start
    print(f"{name} terminé en {duration:.4f} secondes")
