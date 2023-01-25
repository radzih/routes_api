from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional

from src.business.application.common import interfaces
from src.business.application.ticket import exceptions
from src.business.domain import entities
from tests.mocks.repositories.base import BaseRepo


class TicketSaver(interfaces.TicketSaver, BaseRepo):
    async def save_ticket(self, ticket: entities.Ticket) -> entities.TicketId:
        if any(
            (
                ticket.user_id < 0,
                ticket.route_id < 0,
                ticket.from_station_id < 0,
                ticket.to_station_id < 0,
            )
        ):
            raise exceptions.InvalidTicketCreateData

        ticket.price = Decimal(
            abs(ticket.to_station_id - ticket.from_station_id),
        )
        ticket.departure_time = datetime.now()
        ticket.arrival_time = ticket.departure_time + timedelta(days=1)

        if not ticket.id:
            ticket.id = (
                len(self.storage["ticket"]) + len(self.to_commit["ticket"]) + 1
            )

        self.to_commit["ticket"][ticket.id] = ticket

        return ticket.id


class TicketReader(interfaces.TicketReader, BaseRepo):
    async def read_ticket(
        self, ticket_id: entities.TicketId
    ) -> entities.Ticket:
        ticket = self.storage["ticket"].get(ticket_id, None)

        if not ticket:
            raise exceptions.TicketNotExists

        return ticket

    async def read_user_tickets(
        self,
        user_id: entities.UserId,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
    ) -> list[entities.Ticket]:
        tickets = list(self.storage["ticket"].values())[offset:][:limit]
        tickets = [ticket for ticket in tickets if ticket.user_id == user_id]

        if active:
            return [
                ticket
                for ticket in tickets
                if ticket.departure_time < datetime.now() is active
                and ticket.is_booked is False
            ]

        return tickets


class TicketRemover(interfaces.TicketRemover, BaseRepo):
    async def remove_ticket(self, ticket_id: entities.TicketId) -> None:
        ticket = self.storage["ticket"].pop(ticket_id, None)

        if not ticket:
            raise exceptions.TicketNotExists
