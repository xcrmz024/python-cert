from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from proyecto_final_integrador.api.routers import orders as orders_router
from proyecto_final_integrador.infrastructure.database import Base
from proyecto_final_integrador.main import app


# PRUEBAS E2E (flujo completo - login → JWT → crear orden → consultar orden)
def test_orders_e2e() -> None:
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    test_session_local = sessionmaker(bind=engine)
    orders_router.SessionLocal = test_session_local

    client = TestClient(app)

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "admin123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    create_response = client.post(
        "/orders",
        json={
            "customer_name": "Karla",
            "product": "Laptop",
            "quantity": 2,
            "unit_price": "1500.00",
        },
        headers=headers,
    )

    assert create_response.status_code == 201

    order = create_response.json()

    assert order["customer_name"] == "Karla"
    assert order["product"] == "Laptop"
    assert order["total"] == "3000.00"

    get_response = client.get(
        f"/orders/{order['id']}",
        headers=headers,
    )

    assert get_response.status_code == 200
    assert get_response.json()["id"] == order["id"]
