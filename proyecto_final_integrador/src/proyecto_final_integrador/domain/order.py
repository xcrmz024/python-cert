from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    id: int | None
    customer_name: str
    product: str
    quantity: int
    unit_price: Decimal

    # validaciones:
    def __post_init__(self) -> None:
        if not self.customer_name.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        if not self.product.strip():
            raise ValueError("El producto es obligatorio.")

        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if self.unit_price <= 0:
            raise ValueError("El precio unitario debe ser mayor que cero.")

    @property
    def total(self) -> Decimal:  # calc derivado
        return self.unit_price * self.quantity
