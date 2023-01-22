from src.business.application.common import interfaces
from src.business.domain import entities
from src.business.application.user.exceptions import UserNotExists


class MockDBGateway(
    interfaces.Commiter,
    interfaces.UserSaver,
    interfaces.UserReader,
):
    def __init__(self) -> None:
        self.storage = {}

    async def save_user(self, user: entities.User) -> entities.UserId:
        if not user.id:
            user.id = len(self.storage) + 1

        self.storage.update({user.id: user})

        return user.id

    async def read_user(self, user_id: entities.UserId) -> entities.User:
        user = self.storage.get(user_id, None)

        if not user:
            raise UserNotExists

        return user

    async def commit(self) -> None:
        pass
