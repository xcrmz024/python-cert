from sqlalchemy import select
from sqlalchemy.orm import Session

from proyecto_final_integrador.application.ports import OrderRepository
from proyecto_final_integrador.domain.order import Order
from proyecto_final_integrador.infrastructure.models import OrderModel


class SqlAlchemyOrderRepository(OrderRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, order: Order) -> Order:
        model = OrderModel(
            customer_name=order.customer_name,
            product=order.product,
            quantity=order.quantity,
            unit_price=order.unit_price,
        )

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return self._to_domain(model)

    def get_by_id(self, order_id: int) -> Order | None:
        model = self.session.get(OrderModel, order_id)

        if model is None:
            return None

        return self._to_domain(model)

    def get_all(self) -> list[Order]:
        models = self.session.scalars(select(OrderModel)).all()
        return [self._to_domain(model) for model in models]

    @staticmethod
    def _to_domain(model: OrderModel) -> Order:
        return Order(
            id=model.id,
            customer_name=model.customer_name,
            product=model.product,
            quantity=model.quantity,
            unit_price=model.unit_price,
        )
