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
    name: Optional[str] = None, 
    surname: Optional[str] = None,
    email: Optional[str] = None,
) -> None:
    if name:
        user.name = name
    if surname:
        user.surname = surname
    if email:
        user.email = email
