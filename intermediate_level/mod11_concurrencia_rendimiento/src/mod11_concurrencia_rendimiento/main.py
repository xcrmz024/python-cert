import asyncio

from mod11_concurrencia_rendimiento.concurrency import (
    URLS,
    measure_async,
    measure_sync,
    run_cpu_tasks,
)


def main() -> None:
    print("=== Fetcher síncrono ===")
    sync_results, sync_time = measure_sync(URLS)
    print(f"Respuestas: {sync_results}")
    print(f"Tiempo: {sync_time:.2f} segundos")

    print("\n=== Fetcher asíncrono ===")
    async_results, async_time = asyncio.run(measure_async(URLS))
    print(f"Respuestas: {async_results}")
    print(f"Tiempo: {async_time:.2f} segundos")

    print("\n=== Cálculo CPU-bound ===")  # enviado a ProcessPoolExecutor
    numbers = [5_000_000, 5_000_000, 5_000_000, 5_000_000]
    cpu_results = run_cpu_tasks(numbers)
    print(f"Resultados: {cpu_results}")


if __name__ == "__main__":
    main()
