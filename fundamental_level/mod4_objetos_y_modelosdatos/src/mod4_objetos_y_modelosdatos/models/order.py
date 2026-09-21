# 1. dataclass Order (con calculos derivados y comparaciones)
from dataclasses import dataclass


@dataclass
class Order:
    id: int
    product: str
    quantity: int
    unit_price: float

    # validaciones
    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if self.unit_price <= 0:
            raise ValueError("El precio debe ser mayor que 0")

    # calc derivado
    @property
    def total(self) -> float:
        return self.quantity * self.unit_price

    # comparaciones
    def __eq__(self, other) -> bool:
        if not isinstance(other, Order):
            return NotImplemented
        return self.id == other.id

    def __lt__(self, other) -> bool:
        if not isinstance(other, Order):
            return NotImplemented
        return self.total < other.total
