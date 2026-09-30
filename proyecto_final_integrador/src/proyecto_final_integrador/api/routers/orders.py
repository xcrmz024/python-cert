from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from proyecto_final_integrador.api.dependencies import get_current_user
from proyecto_final_integrador.api.schemas import OrderCreate, OrderResponse
from proyecto_final_integrador.application.order_service import OrderService
from proyecto_final_integrador.infrastructure.database import SessionLocal
from proyecto_final_integrador.infrastructure.repositories import (
    SqlAlchemyOrderRepository,
)

# router orders: (enpoints operaciones http orders)
router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


def build_order_response(order) -> OrderResponse:
    return OrderResponse(
        id=order.id,
        customer_name=order.customer_name,
        product=order.product,
        quantity=order.quantity,
        unit_price=order.unit_price,
        total=order.total,
    )


# POST /orders
@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    data: OrderCreate,
    _: Annotated[str, Depends(get_current_user)],
) -> OrderResponse:
    session = SessionLocal()

    try:
        service = OrderService(
            SqlAlchemyOrderRepository(session),
        )

        order = service.create_order(
            customer_name=data.customer_name,
            product=data.product,
            quantity=data.quantity,
            unit_price=str(data.unit_price),
        )

        return build_order_response(order)
    finally:
        session.close()


# GET  /orders
@router.get(
    "",
    response_model=list[OrderResponse],
)
def get_orders(
    _: Annotated[str, Depends(get_current_user)],
) -> list[OrderResponse]:
    session = SessionLocal()

    try:
        service = OrderService(
            SqlAlchemyOrderRepository(session),
        )

        return [build_order_response(order) for order in service.get_orders()]
    finally:
        session.close()


# GET  /orders/{order_id}
@router.get(
    "/{order_id}",
    response_model=OrderResponse,
)
def get_order(
    order_id: int,
    _: Annotated[str, Depends(get_current_user)],
) -> OrderResponse:
    session = SessionLocal()

    try:
        service = OrderService(
            SqlAlchemyOrderRepository(session),
        )

        try:
            order = service.get_order(order_id)
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(exc),
            ) from exc

        return build_order_response(order)
    finally:
        session.close()
