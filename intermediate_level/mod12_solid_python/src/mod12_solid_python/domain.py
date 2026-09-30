from dataclasses import dataclass


@dataclass
class Order:
    id: int
    product: str
    quantity: int
