from decimal import Decimal

from pydantic import BaseModel, Field


# Esquemas Pydantic: (validacion de datos entrantes a API)
class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100)
    product: str = Field(min_length=1, max_length=100)
    quantity: int = Field(gt=0)
    unit_price: Decimal = Field(gt=0)


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    product: str
    quantity: int
    unit_price: Decimal
    total: Decimal
