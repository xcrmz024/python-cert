from typing import Protocol

from .domain import Order


# puerto:
class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...

    def get(self, order_id: int) -> Order | None: ...
