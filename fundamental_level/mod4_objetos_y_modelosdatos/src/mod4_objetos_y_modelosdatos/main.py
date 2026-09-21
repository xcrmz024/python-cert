from models.order_schema import OrderIn, OrderOut

order_data = OrderIn(
    product="Teclado",
    quantity=3,
    unit_price=25.50,
)

order = order_data.to_entity(order_id=1)

order_out = OrderOut.from_entity(order)

print(order)
print(f"Total: {order.total}")
print(order_out.model_dump())

orders = [
    OrderIn(product="Monitor", quantity=1, unit_price=200).to_entity(2),
    OrderIn(product="Ratón", quantity=2, unit_price=25).to_entity(3),
    OrderIn(product="Teclado", quantity=3, unit_price=25.50).to_entity(1),
]

orders.sort()

for item in orders:
    print(item.product, item.total)

# OrderOut
# invalid_output = OrderOut(
# id=1,
# product="Teclado",
# quantity=3,
# unit_price=25.50,
# total=-10,
# )

# print(invalid_output)
