from dataclasses import asdict

from src.business.application.common.use_cases import UseCase
from src.business.application.user import dto
from src.business.application.user.interfaces import DBGateway
from src.business.domain import entities
from src.business.domain.services import create_user, update_user


class CreateUser(UseCase):
    def __init__(self, db_gateway: DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.UserCreate) -> entities.UserId:
        user = create_user(
            name=data.name,
            surname=data.surname,
            email=data.email,
        )

        user_id = await self.db_gateway.save_user(user)
        await self.db_gateway.commit()

        return user_id


class GetUser(UseCase):
    def __init__(self, db_gateway: DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.UserId) -> dto.User:
        user = await self.db_gateway.read_user(data)

        return dto.User(**asdict(user))


class UpdateUser(UseCase):
    def __init__(self, db_gateway: DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.UserUpdate) -> dto.User:
        user = await self.db_gateway.read_user(data.id)

        update_user(user, data.name, data.surname, data.email)

        await self.db_gateway.save_user(user)
        await self.db_gateway.commit()

        return dto.User(**asdict(user))
