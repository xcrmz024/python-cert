import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

import httpx

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]


# sincrona
def fetch_sync(urls: list[str]) -> list[int]:
    results = []

    with httpx.Client(timeout=10.0) as client:
        for url in urls:
            response = client.get(url)
            results.append(response.status_code)

    return results


# asincrona (+ async/await)
async def fetch_async(urls: list[str], max_concurrent: int = 3) -> list[int]:
    semaphore = asyncio.Semaphore(max_concurrent)

    async with httpx.AsyncClient(timeout=10.0) as client:

        async def fetch(url: str) -> int:
            async with semaphore:
                response = await client.get(url)
                return response.status_code

        return await asyncio.gather(*(fetch(url) for url in urls))


def cpu_task(number: int) -> int:  # CPU bound
    total = 0

    for value in range(number):
        total += value * value

    return total


# CPU bound con ProcessPoolExcecutor:
def run_cpu_tasks(numbers: list[int]) -> list[int]:
    with ProcessPoolExecutor() as executor:
        return list(executor.map(cpu_task, numbers))


def measure_sync(urls: list[str]) -> tuple[list[int], float]:
    start = time.perf_counter()
    results = fetch_sync(urls)
    elapsed = time.perf_counter() - start
    return results, elapsed


async def measure_async(
    urls: list[str],
) -> tuple[list[int], float]:
    start = time.perf_counter()
    results = await fetch_async(urls)
    elapsed = time.perf_counter() - start
    return results, elapsed
