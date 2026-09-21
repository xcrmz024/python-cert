# 2. Modelos Pydantic (OrderIn/OrderOut) y conversión a entidad:
from pydantic import BaseModel, Field

from .order import Order


# OrderIn
class OrderIn(BaseModel):
    product: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    # conversion a entidad
    def to_entity(self, order_id: int) -> Order:
        return Order(
            id=order_id,
            product=self.product,
            quantity=self.quantity,
            unit_price=self.unit_price,
        )


# OrderOut
class OrderOut(BaseModel):
    id: int
    product: str
    quantity: int
    unit_price: float
    total: float = Field(gt=0)

    # conversion de entidad
    @classmethod
    def from_entity(cls, order: Order) -> "OrderOut":
        return cls(
            id=order.id,
            product=order.product,
            quantity=order.quantity,
            unit_price=order.unit_price,
            total=order.total,
        )
