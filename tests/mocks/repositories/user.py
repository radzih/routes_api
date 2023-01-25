from src.business.application.common import interfaces
from src.business.application.user import exceptions
from src.business.domain import entities
from tests.mocks.repositories.base import BaseRepo


class UserSaver(interfaces.UserReader, BaseRepo):
    async def save_user(self, user: entities.User) -> entities.UserId:
        if not user.id:
            user.id = (
                len(self.storage["user"]) + len(self.to_commit["user"]) + 1
            )

        self.to_commit["user"].update({user.id: user})

        return user.id


class UserReader(interfaces.UserReader, BaseRepo):
    async def read_user(self, user_id: entities.UserId) -> entities.User:
        user = self.storage["user"].get(user_id, None)

        if not user:
            raise exceptions.UserNotExists

        return user
