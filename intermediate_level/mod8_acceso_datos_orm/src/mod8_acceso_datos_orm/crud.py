from sqlalchemy import select
from sqlalchemy.orm import joinedload

from mod8_acceso_datos_orm.database import SessionLocal
from mod8_acceso_datos_orm.models import Order, OrderItem, User


# CREATE INSERT
def create_user(name: str, email: str) -> User:
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


# READ
def get_user(user_id: int) -> User | None:
    with SessionLocal() as session:
        return session.get(User, user_id)


def get_users() -> list[User]:
    with SessionLocal() as session:
        statement = select(User)
        return list(session.scalars(statement))


# UPDATE
def update_user(user_id: int, name: str) -> User | None:
    with SessionLocal() as session:
        user = session.get(User, user_id)

        if user is None:
            return None

        user.name = name
        session.commit()
        session.refresh(user)

        return user


# DELETE
def delete_user(user_id: int) -> bool:
    with SessionLocal() as session:
        user = session.get(User, user_id)

        if user is None:
            return False

        session.delete(user)
        session.commit()

        return True


# ORDERS:
# CREATE- INSERT
def create_order(
    user_id: int,
    description: str,
    products: list[tuple[str, int]],
) -> Order:
    with SessionLocal() as session:
        user = session.get(User, user_id)

        if user is None:
            raise ValueError("User not found")

        order = Order(
            description=description,
            user=user,
        )

        for product, quantity in products:
            order.items.append(
                OrderItem(
                    product=product,
                    quantity=quantity,
                )
            )

        session.add(order)
        session.commit()
        session.refresh(order)

        return order


# READ
def get_order(order_id: int) -> Order | None:
    with SessionLocal() as session:
        statement = (
            select(Order)
            .options(
                joinedload(Order.user),
                joinedload(Order.items),
            )
            .where(Order.id == order_id)
        )

        return session.scalars(statement).first()
