from mod7_http_consumo_apis.client import download_file


def main() -> None:
    download_file(
        "https://httpbin.org/bytes/1024",
        "downloads/test.bin",
    )


# prueba client: get_data("https://httpbin.org/get")#prueba clientes http
# prueba excepc http: get_data("https://httpbin.org/status/404")
# prueba error de conexión: get_data("http://localhost:9999")

download_file(
    "https://httpbin.org/bytes/1024",
    "downloads/test.bin",
)
if __name__ == "__main__":
    main()
