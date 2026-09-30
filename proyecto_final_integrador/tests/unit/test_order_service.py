from proyecto_final_integrador.application.order_service import OrderService
from proyecto_final_integrador.domain.order import Order


# Pruebas unitarias (casos de uso):
class FakeOrderRepository:
    def __init__(self) -> None:
        self.orders: list[Order] = []

    def save(self, order: Order) -> Order:
        order.id = len(self.orders) + 1
        self.orders.append(order)
        return order

    def get_by_id(self, order_id: int) -> Order | None:
        return next(
            (order for order in self.orders if order.id == order_id),
            None,
        )

    def get_all(self) -> list[Order]:
        return self.orders


def test_create_order() -> None:
    repository = FakeOrderRepository()
    service = OrderService(repository)

    order = service.create_order(
        customer_name="Karla",
        product="Laptop",
        quantity=2,
        unit_price="1500.00",
    )

    assert order.id == 1
    assert order.total == 3000


def test_get_order() -> None:
    repository = FakeOrderRepository()
    service = OrderService(repository)

    created = service.create_order(
        customer_name="Karla",
        product="Mouse",
        quantity=1,
        unit_price="250.00",
    )

    order = service.get_order(created.id)

    assert order.product == "Mouse"


def test_get_order_not_found() -> None:
    repository = FakeOrderRepository()
    service = OrderService(repository)

    try:
        service.get_order(999)
    except ValueError as exc:
        assert str(exc) == "Orden no encontrada."
    else:
        raise AssertionError("Se esperaba ValueError")
