import os
from datetime import UTC, datetime, timedelta

import jwt

# JWT:
SECRET_KEY = os.getenv(
    "ORDERS_SECRET_KEY",
    "development-only-secret-key-change-in-production",
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DEMO_USERNAME = "admin"
DEMO_PASSWORD = "admin123"


def authenticate_user(username: str, password: str) -> bool:
    return username == DEMO_USERNAME and password == DEMO_PASSWORD


def create_access_token(username: str) -> str:
    expires_at = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": username,
        "exp": expires_at,
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> str:
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )

    username = payload.get("sub")

    if not username:
        raise ValueError("Token inválido.")

    return str(username)
