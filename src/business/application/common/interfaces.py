from typing import Protocol

from src.business.domain import entities


class Commiter(Protocol):
    async def commit(self) -> None:
        ...


class UserReader(Protocol):
    async def read_user(self, user_id: entities.UserId) -> entities.User:
        ...


class UserSaver(Protocol):
    async def save_user(self, user: entities.User) -> entities.UserId:
        ...
