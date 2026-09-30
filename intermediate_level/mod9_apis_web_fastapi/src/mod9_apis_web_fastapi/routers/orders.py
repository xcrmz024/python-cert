from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from ..auth import decode_access_token
from ..database import get_db
from ..models import Order
from ..schemas import OrderCreate, OrderOut

# CRUD Orders protegido con JWT
router = APIRouter(prefix="/orders", tags=["Orders"])
security = HTTPBearer()
security_dependency = Depends(security)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = security_dependency,
) -> str:
    username = decode_access_token(credentials.credentials)

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    return username


db_dependency = Depends(get_db)
user_dependency = Depends(get_current_user)


@router.post(
    "/",
    response_model=OrderOut,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    order_data: OrderCreate,
    db: Session = db_dependency,
    _: str = user_dependency,
) -> Order:
    order = Order(
        product=order_data.product,
        quantity=order_data.quantity,
        total=order_data.total,
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


@router.get("/", response_model=list[OrderOut])
def get_orders(
    db: Session = db_dependency,
    _: str = user_dependency,
) -> list[Order]:
    return db.query(Order).all()


@router.get("/{order_id}", response_model=OrderOut)
def get_order(
    order_id: int,
    db: Session = db_dependency,
    _: str = user_dependency,
) -> Order:
    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return order


@router.put("/{order_id}", response_model=OrderOut)
def update_order(
    order_id: int,
    order_data: OrderCreate,
    db: Session = db_dependency,
    _: str = user_dependency,
) -> Order:
    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    order.product = order_data.product
    order.quantity = order_data.quantity
    order.total = order_data.total

    db.commit()
    db.refresh(order)

    return order


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(
    order_id: int,
    db: Session = db_dependency,
    _: str = user_dependency,
) -> None:
    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    db.delete(order)
    db.commit()
