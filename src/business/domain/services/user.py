from typing import Optional

from src.business.domain import entities


def create_user(name: str, surname: str, email: str) -> entities.User:
    return entities.User(
        id=None,
        name=name,
        surname=surname,
        email=email,
    )


def update_user(
    user: entities.User,
    name: Optional[str],
    surname: Optional[str],
    email: Optional[str],
) -> None:
    if name:
        user.name = name
    if surname:
        user.surname = surname
    if email:
        user.email = surname
