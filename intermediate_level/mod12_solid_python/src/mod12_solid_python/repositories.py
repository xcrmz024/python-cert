import sqlite3

from .domain import Order


# implementación sql (sqlite3):
class InMemoryOrderRepository:
    def __init__(self) -> None:
        self.orders: dict[int, Order] = {}

    def save(self, order: Order) -> None:
        self.orders[order.id] = order

    def get(self, order_id: int) -> Order | None:
        return self.orders.get(order_id)


class SqlOrderRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                product TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
            """)
        self.connection.commit()

    def save(self, order: Order) -> None:
        self.connection.execute(
            """
            INSERT OR REPLACE INTO orders (id, product, quantity)
            VALUES (?, ?, ?)
            """,
            (order.id, order.product, order.quantity),
        )
        self.connection.commit()

    def get(self, order_id: int) -> Order | None:
        row = self.connection.execute(
            "SELECT id, product, quantity FROM orders WHERE id = ?",
            (order_id,),
        ).fetchone()

        if row is None:
            return None

        return Order(id=row[0], product=row[1], quantity=row[2])
