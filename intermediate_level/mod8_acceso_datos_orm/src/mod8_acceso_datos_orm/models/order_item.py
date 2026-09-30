from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mod8_acceso_datos_orm.database import Base

if TYPE_CHECKING:
    from mod8_acceso_datos_orm.models.order import Order


# order_item entity:
class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    product: Mapped[str]
    quantity: Mapped[int]

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    order: Mapped["Order"] = relationship(back_populates="items")
