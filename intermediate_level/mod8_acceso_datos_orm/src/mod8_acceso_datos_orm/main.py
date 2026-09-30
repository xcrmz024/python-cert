from mod8_acceso_datos_orm.crud import create_order, create_user, get_order

user = create_user("Juan", "juan@example.com")

order = create_order(
    user.id,
    "Compra de accesorios",
    [
        ("Teclado", 1),
        ("Mouse", 2),
        ("Audífonos", 1),
    ],
)

print("ORDEN:", order.id, order.description)

order = get_order(order.id)

print("USUARIO:", order.user.name)

print("PRODUCTOS:")

for item in order.items:
    print("-", item.product, "x", item.quantity)
