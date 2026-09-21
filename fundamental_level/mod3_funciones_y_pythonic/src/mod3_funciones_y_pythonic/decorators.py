# 1. Decorador de reintentos con backoff
# funciones, *args, **kwargs, closures, decoradores

# funcion decoradora
import time


def retry(max_retries, backoff=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_retries - 1:
                        raise

                    wait_time = backoff * (2**attempt)  # backoff
                    time.sleep(wait_time)

        return wrapper

    return decorator
