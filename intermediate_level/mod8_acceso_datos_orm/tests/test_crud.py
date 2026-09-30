from mod8_acceso_datos_orm.crud import (
    create_order,
    create_user,
    delete_user,
    get_order,
    update_user,
)


# CREATE INSERT
def test_create_order():
    user = create_user("Test User", "test@example.com")

    order = create_order(
        user.id,
        "Test order",
        [
            ("Keyboard", 1),
            ("Mouse", 2),
        ],
    )
    # READ
    saved_order = get_order(order.id)

    assert saved_order is not None
    assert saved_order.description == "Test order"
    assert saved_order.user.name == "Test User"
    assert len(saved_order.items) == 2


# UPDATE
def test_update_user():
    user = create_user("Old Name", "update@example.com")

    updated_user = update_user(user.id, "New Name")

    assert updated_user is not None
    assert updated_user.name == "New Name"


# DELETE
def test_delete_user():
    user = create_user("Delete User", "delete@example.com")

    result = delete_user(user.id)

    assert result is True
