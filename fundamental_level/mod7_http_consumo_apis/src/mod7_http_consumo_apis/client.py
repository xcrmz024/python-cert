import httpx
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_fixed


# ---1. Cliente http:---
# reintento
def is_retryable_error(error: BaseException) -> bool:
    if isinstance(error, httpx.HTTPStatusError):
        return error.response.status_code in {502, 503, 504}

    return isinstance(error, httpx.RequestError)


@retry(
    retry=retry_if_exception(is_retryable_error),
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
)
def request_data(url: str) -> httpx.Response:
    with httpx.Client(timeout=5.0) as client:  # timeout
        response = client.get(url)
        response.raise_for_status()

        return response


def get_data(url: str) -> None:
    try:
        response = request_data(url)

        print(f"Status: {response.status_code}")
        print(f"Body: {response.text}")

    except httpx.TimeoutException:
        print("La petición excedió el tiempo límite.")

    except httpx.HTTPStatusError as error:
        print(f"Error HTTP: {error.response.status_code}")


# ---2. descarga por streaming a disco:---
# reintentos por streaming
@retry(
    retry=retry_if_exception(is_retryable_error),
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
)
def download_file(url: str, destination: str) -> None:
    with httpx.Client(timeout=5.0) as client, client.stream("GET", url) as response:
        response.raise_for_status()

        with open(destination, "wb") as file:
            file.writelines(response.iter_bytes())
