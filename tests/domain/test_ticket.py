from src.business.domain import services, entities


def test_create_ticket() -> None:
    ticket = services.create_ticket(1, 1, 1, 4, False)

    assert isinstance(ticket, entities.Ticket)
    assert ticket.route_id == 1
    assert ticket.from_station_id == 1
    assert ticket.to_station_id == 4
    assert ticket.is_booked == False

def test_ticket() -> None:
    ticket = services.create_ticket(1, 1, 1, 4, True)

    ticket.unbook_ticket()

    assert ticket.is_booked is False