import asyncio
import socket
import threading

import aiohttp
import pytest
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from mod9_apis_web_fastapi.database import Base, get_db
from mod9_apis_web_fastapi.main import app

# test integración (login + JWT + crud + db temporal sqlite)


def get_free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


@pytest.fixture
def server():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = testing_session()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    port = get_free_port()
    config = uvicorn.Config(
        app,
        host="127.0.0.1",
        port=port,
        log_level="error",
    )
    server_instance = uvicorn.Server(config)

    thread = threading.Thread(
        target=server_instance.run,
        daemon=True,
    )
    thread.start()

    for _ in range(50):
        if server_instance.started:
            break
        asyncio.run(asyncio.sleep(0.1))

    yield f"http://127.0.0.1:{port}"

    server_instance.should_exit = True
    thread.join(timeout=5)
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.mark.asyncio
async def test_orders_crud(server):
    async with aiohttp.ClientSession() as client:
        async with client.post(
            f"{server}/auth/login",
            json={
                "username": "admin",
                "password": "admin123",
            },
        ) as response:
            assert response.status == 200
            login_data = await response.json()

        token = login_data["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        async with client.post(
            f"{server}/orders/",
            json={
                "product": "Keyboard",
                "quantity": 2,
                "total": 100,
            },
            headers=headers,
        ) as response:
            assert response.status == 201
            order = await response.json()

        order_id = order["id"]

        async with client.get(
            f"{server}/orders/{order_id}",
            headers=headers,
        ) as response:
            assert response.status == 200
            data = await response.json()
            assert data["product"] == "Keyboard"

        async with client.put(
            f"{server}/orders/{order_id}",
            json={
                "product": "Keyboard Pro",
                "quantity": 3,
                "total": 150,
            },
            headers=headers,
        ) as response:
            assert response.status == 200
            data = await response.json()
            assert data["product"] == "Keyboard Pro"

        async with client.delete(
            f"{server}/orders/{order_id}",
            headers=headers,
        ) as response:
            assert response.status == 204
