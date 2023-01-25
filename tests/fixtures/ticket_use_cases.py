from pytest import fixture

from src.business.application.ticket import use_cases
from tests.mocks.db import MockDBGateway


@fixture
def get_ticket(db_gateway: MockDBGateway) -> use_cases.GetTicket:
    return use_cases.GetTicket(db_gateway)


@fixture
def book_ticket(db_gateway: MockDBGateway) -> use_cases.BookTicket:
    return use_cases.BookTicket(db_gateway)


@fixture
def unbook_ticket(db_gateway: MockDBGateway) -> use_cases.UnbookTicket:
    return use_cases.UnbookTicket(db_gateway)


@fixture
def delete_ticket(db_gateway: MockDBGateway) -> use_cases.DeleteTicket:
    return use_cases.DeleteTicket(db_gateway)


@fixture
def get_user_active_tickets(
    db_gateway: MockDBGateway,
) -> use_cases.GetUserActiveTickets:
    return use_cases.GetUserActiveTickets(db_gateway)


@fixture
def get_user_inactive_tickets(
    db_gateway: MockDBGateway,
) -> use_cases.GetUserInactiveTickets:
    return use_cases.GetUserInactiveTickets(db_gateway)
