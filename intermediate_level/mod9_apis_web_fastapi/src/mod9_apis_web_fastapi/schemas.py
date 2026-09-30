from pydantic import BaseModel, ConfigDict, Field


# Esquemas para validación:
class OrderBase(BaseModel):
    product: str = Field(min_length=1, max_length=100)
    quantity: int = Field(gt=0)
    total: float = Field(gt=0)


class OrderCreate(OrderBase):
    pass


class OrderOut(OrderBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
