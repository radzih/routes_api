from datetime import datetime

from pytest import raises

from src.business.application.ticket import dto, exceptions, use_cases
from tests.mocks.db import MockDBGateway


class TestTicket:
    async def test_book_ticket(
        self, book_ticket: use_cases.BookTicket
    ) -> None:
        ticket = await book_ticket(
            dto.TicketBook(
                route_id=1, user_id=1, from_station_id=1, to_station_id=5
            )
        )

        assert ticket.route_id == 1
        assert ticket.user_id == 1
        assert ticket.is_booked is True

        with raises(exceptions.InvalidTicketCreateData):
            await book_ticket(
                dto.TicketBook(
                    route_id=-1, user_id=-1, from_station_id=1, to_station_id=5
                )
            )

        with raises(exceptions.InvalidTicketCreateData):
            await book_ticket(
                dto.TicketBook(
                    route_id=1, user_id=-1, from_station_id=1, to_station_id=5
                )
            )

    async def test_get_ticket(self, get_ticket: use_cases.GetTicket) -> None:
        ticket = await get_ticket(1)

        assert ticket.id == 1
        assert ticket.departure_time < datetime.now()

        with raises(exceptions.TicketNotExists):
            await get_ticket(-100)

    async def test_unbook_ticket(
        self, unbook_ticket: use_cases.UnbookTicket
    ) -> None:
        ticket = await unbook_ticket(1)

        assert ticket.is_booked is False

        with raises(exceptions.TicketNotExists):
            await unbook_ticket(-100)

    async def test_delete_ticket(
        self,
        delete_ticket: use_cases.DeleteTicket,
        get_ticket: use_cases.GetTicket,
    ) -> None:
        with raises(exceptions.TicketNotExists):
            await delete_ticket(-1)

        await delete_ticket(1)

    async def test_get_user_active_tickets(
        self,
        get_user_active_tickets: use_cases.GetUserActiveTickets,
        db_gateway: MockDBGateway,
    ):
        db_gateway.clean_db()
        db_gateway.fill_storage()
        tickets = await get_user_active_tickets(dto.TicketsGet(1, 100, 0))

        assert len(tickets) == 0

    async def test_get_user_inactive_tickets(
        self, get_user_inactive_tickets: use_cases.GetUserInactiveTickets
    ):
        tickets = await get_user_inactive_tickets(dto.TicketsGet(1, 100, 0))

        assert len(tickets) == 2
