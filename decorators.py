# decorators.py
# Very small helper functions. Kept tiny and readable.

import time
import functools

def simple_timer(func):
    """Decorator to print how long the function took to run."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMER] {func.__name__} took {elapsed:.2f}s")
        return result
    return wrapped

class Logger:
    """Tiny logger mixin to show how a class can provide logging."""
    def log(self, msg):
        print(f"[LOG] {msg}")
 