from typing import Protocol, Optional

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


class TicketReader(Protocol):
    async def read_user_tickets(
        self,
        user_id: entities.UserId,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
    ) -> list[entities.Ticket]:
        ...

    async def read_ticket(
        self,
        ticket_id: entities.TicketId,
    ) -> entities.Ticket:
        ...


class TicketSaver(Protocol):
    async def save_ticket(self, ticket: entities.Ticket) -> entities.TicketId:
        ...


class TicketRemover(Protocol):
    async def remove_ticket(self, ticket_id: entities.TicketId) -> None:
        ...
