from src.business.domain import services, entities


def test_create_user() -> None:
    name = "John"
    surname = "Doe"
    email = "example@mail.com"

    user = services.create_user(name, surname, email)

    assert user.name == name
    assert user.surname == surname
    assert user.email == email


def test_update_user() -> None:
    name = "John"
    surname = "Doe"
    email = "example@mail.com"

    user = services.create_user(name, surname, email)

    new_name = "Bill"
    new_surname = "Marker"
    new_email = "newmail@mail.com"

    services.update_user(user)

    assert isinstance(user, entities.User)
    assert user.name == name
    assert user.surname == surname
    assert user.email == email

    services.update_user(user, new_name)

    assert user.name == new_name
    assert user.surname == surname
    assert user.email == email

    services.update_user(user, surname=new_surname)

    assert user.name == new_name
    assert user.surname == new_surname
    assert user.email == email

    services.update_user(user, email=new_email)

    assert user.name == new_name
    assert user.surname == new_surname
    assert user.email == new_email
