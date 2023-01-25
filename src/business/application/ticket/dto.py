from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from src.business.domain import entities


@dataclass
class TicketBook:
    route_id: entities.RouteId
    user_id: entities.UserId
    from_station_id: entities.StationId
    to_station_id: entities.StationId


@dataclass
class Ticket:
    id: entities.TicketId
    route_id: entities.RouteId
    user_id: entities.UserId
    from_station_id: entities.StationId
    to_station_id: entities.StationId
    price: Decimal
    departure_time: datetime
    arrival_time: datetime
    is_booked: bool


@dataclass
class TicketsGet:
    user_id: entities.UserId
    limit: int
    offset: int
