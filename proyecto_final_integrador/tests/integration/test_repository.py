from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from proyecto_final_integrador.domain.order import Order
from proyecto_final_integrador.infrastructure.database import Base
from proyecto_final_integrador.infrastructure.repositories import (
    SqlAlchemyOrderRepository,
)


# PRUEBAS INTEGRACIÓN (SQLAlchemy + repositorio + base de datos)
def test_repository_save_and_get() -> None:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    session_local = sessionmaker(bind=engine)
    session = session_local()

    repository = SqlAlchemyOrderRepository(session)

    order = Order(
        id=None,
        customer_name="Karla",
        product="Laptop",
        quantity=2,
        unit_price=Decimal("1500.00"),
    )

    saved_order = repository.save(order)
    found_order = repository.get_by_id(saved_order.id)

    assert found_order is not None
    assert found_order.customer_name == "Karla"
    assert found_order.product == "Laptop"
    assert found_order.total == Decimal("3000.00")

    session.close()
