from typing import Protocol

from proyecto_final_integrador.domain.order import Order


# puerto con protcol:
class OrderRepository(Protocol):
    def save(self, order: Order) -> Order: ...

    def get_by_id(self, order_id: int) -> Order | None: ...

    def get_all(self) -> list[Order]: ...
