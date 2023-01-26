from dataclasses import asdict
from decimal import Decimal

from src.business.application.common import use_cases
from src.business.application.ticket import dto, interfaces
from src.business.domain import entities, services


class BookTicket(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.TicketBook) -> dto.Ticket:
        ticket = services.create_ticket(**asdict(data), is_booked=True)

        ticket_id = await self.db_gateway.save_ticket(ticket)
        await self.db_gateway.commit()
        ticket = await self.db_gateway.read_ticket(ticket_id)

        return dto.Ticket(**asdict(ticket))


class GetTicket(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.TicketId) -> dto.Ticket:
        ticket = await self.db_gateway.read_ticket(data)

        return dto.Ticket(**asdict(ticket))


class UnbookTicket(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.TicketId) -> dto.Ticket:
        ticket = await self.db_gateway.read_ticket(data)

        ticket.unbook_ticket()

        await self.db_gateway.save_ticket(ticket)
        await self.db_gateway.commit()

        return dto.Ticket(**asdict(ticket))


class GetUserActiveTickets(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.TicketsGet) -> list[dto.Ticket]:
        await self.db_gateway.read_user(data.user_id)
        tickets = await self.db_gateway.read_user_tickets(
            user_id=data.user_id,
            limit=data.limit,
            offset=data.offset,
            active=True,
        )

        return [dto.Ticket(**asdict(ticket)) for ticket in tickets]


class GetUserInactiveTickets(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.TicketsGet) -> list[dto.Ticket]:
        await self.db_gateway.read_user(data.user_id)
        tickets = await self.db_gateway.read_user_tickets(
            user_id=data.user_id,
            limit=data.limit,
            offset=data.offset,
            active=False,
        )

        return [dto.Ticket(**asdict(ticket)) for ticket in tickets]


class DeleteTicket(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.TicketId) -> None:
        await self.db_gateway.remove_ticket(data)
        await self.db_gateway.commit()


class GetTicketPrice(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.TicketPriceGet) -> Decimal:
        ticket_price = await self.db_gateway.read_ticket_price(**asdict(data))
        return ticket_price
