from .domain import Order
from .ports import OrderRepository


class OrderService:
    def __init__(
        self, repository: OrderRepository
    ) -> None:  # Refactor de servicio para depender de puerto (Protocol)
        self.repository = repository

    def create_order(self, order: Order) -> None:
        self.repository.save(order)

    def find_order(self, order_id: int) -> Order | None:
        return self.repository.get(order_id)
