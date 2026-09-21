from typing import Literal, Protocol, TypedDict

from mod5_tipado_estatico_calidad.models.order import Order
from mod5_tipado_estatico_calidad.models.order_schema import OrderIn, OrderOut


# --Union:--
def format_order_id(order_id: int | str) -> str:
    return f"Order ID: {order_id}"


print(format_order_id(123))  # prueba union (int)
print(format_order_id("ORD-001"))  # prueba union (str)


# --Literal:--
def get_status_message(status: Literal["pending", "completed", "cancelled"]) -> str:
    return f"Order status: {status}"


get_status_message("pending")  # prueba literal (valido)
get_status_message("completed")  # prueba literal (valido)
# print(get_status_message("unknown"))#prueba literal (invalido)


# --TypedDict:--
class OrderData(TypedDict):
    product: str
    quantity: int
    unit_price: float


def create_order(data: OrderData) -> Order:  # data: TypeDict
    return Order(
        id=1,
        product=data["product"],
        quantity=data["quantity"],
        unit_price=data["unit_price"],
    )


# probar typedDict
order_data: OrderData = {
    "product": "Teclado",  # str (valido)
    "quantity": 3,  # int (valido)
    "unit_price": 25.50,  # float (valido)
}
new_order = create_order(order_data)
print(new_order)


# --Protocol:--
class OrderLike(Protocol):
    product: str
    quantity: int

    @property
    def total(self) -> float: ...


def print_order_summary(order: OrderLike) -> str:
    return f"{order.product}: {order.total}"


order_input = OrderIn(
    product="Teclado",
    quantity=3,
    unit_price=25.50,
)

order: Order = order_input.to_entity(order_id=1)

print(print_order_summary(order))

order_out = OrderOut.from_entity(order)

print(order)
print(f"Total: {order.total}")
print(order_out.model_dump())

# tipado estatico en lista:
orders: list[Order] = [  # changed: orders: [] -> orders: list[Order] =[]
    OrderIn(product="Monitor", quantity=1, unit_price=200).to_entity(2),
    OrderIn(product="Ratón", quantity=2, unit_price=25).to_entity(3),
    OrderIn(product="Teclado", quantity=3, unit_price=25.50).to_entity(1),
]

orders.sort()

for item in orders:
    print(
        item.product, item.total
    )  # mypy style error ex: (...+ item.email), (order has no email atribute)

# OrderOut
# invalid_output = OrderOut(
# id=1,
# product="Teclado",
# quantity=3,
# unit_price=25.50,
# total=-10,
# )

# print(invalid_output)
