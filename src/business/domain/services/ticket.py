from src.business.domain import entities


def create_ticket(
    route_id: entities.RouteId,
    user_id: entities.UserId,
    from_station_id: entities.StationId,
    to_station_id: entities.StationId,
    is_booked: bool
) -> entities.Ticket:
    return entities.Ticket(
        id=None,
        route_id=route_id,
        user_id=user_id,
        from_station_id=from_station_id,
        to_station_id=to_station_id,
        price=None,
        departure_time=None,
        arrival_time=None,
        is_booked=is_booked,
    )
