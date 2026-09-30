import sqlite3

from .domain import Order
from .repositories import InMemoryOrderRepository, SqlOrderRepository
from .service import OrderService


# verificaciín LSP:
def verify_repository(repository: object) -> None:
    service = OrderService(repository)

    order = Order(id=1, product="Laptop", quantity=2)
    service.create_order(order)

    result = service.find_order(1)

    assert result == order
    print(f"OK: {type(repository).__name__}")


def main() -> None:
    verify_repository(InMemoryOrderRepository())

    connection = sqlite3.connect(":memory:")
    verify_repository(SqlOrderRepository(connection))
    connection.close()

    print("LSP verificado: ambas implementaciones son sustituibles.")


if __name__ == "__main__":
    main()
