from proyecto_final_integrador.application.ports import OrderRepository
from proyecto_final_integrador.domain.order import Order


# casos de uso:
class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    def create_order(
        self,
        customer_name: str,
        product: str,
        quantity: int,
        unit_price: str,
    ) -> Order:
        from decimal import Decimal

        order = Order(
            id=None,
            customer_name=customer_name,
            product=product,
            quantity=quantity,
            unit_price=Decimal(unit_price),
        )

        return self.repository.save(order)

    def get_order(self, order_id: int) -> Order:
        order = self.repository.get_by_id(order_id)

        if order is None:
            raise ValueError("Orden no encontrada.")

        return order

    def get_orders(self) -> list[Order]:
        return self.repository.get_all()
