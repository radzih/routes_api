from src.business.domain import entities


def create_user(name: str, surname: str, email: str) -> entities.User:
    return entities.User(
        id=None,
        name=name,
        surname=surname, 
        email=email,
    )
