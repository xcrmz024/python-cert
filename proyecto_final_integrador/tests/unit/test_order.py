from decimal import Decimal

import pytest

from proyecto_final_integrador.domain.order import Order


# Pruebas unitarias (dominio order):
def test_order_calculates_total() -> None:
    order = Order(
        id=1,
        customer_name="Karla",
        product="Laptop",
        quantity=2,
        unit_price=Decimal("1500.00"),
    )

    assert order.total == Decimal("3000.00")


def test_order_rejects_invalid_quantity() -> None:
    with pytest.raises(ValueError, match="cantidad"):
        Order(
            id=1,
            customer_name="Karla",
            product="Laptop",
            quantity=0,
            unit_price=Decimal("1500.00"),
        )


def test_order_rejects_invalid_price() -> None:
    with pytest.raises(ValueError, match="precio"):
        Order(
            id=1,
            customer_name="Karla",
            product="Laptop",
            quantity=1,
            unit_price=Decimal(0),
        )


def test_order_rejects_empty_customer() -> None:
    with pytest.raises(ValueError, match="cliente"):
        Order(
            id=1,
            customer_name="",
            product="Laptop",
            quantity=1,
            unit_price=Decimal("1500.00"),
        )
