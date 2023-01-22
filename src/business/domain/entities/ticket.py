from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import NewType, Optional

from .route import RouteId
from .station import StationId
from .user import UserId

TicketId = NewType("TicketId", int)


@dataclass
class Ticket:
    id: Optional[TicketId]
    route_id: RouteId
    user_id: UserId
    from_station_id: StationId
    to_station_id: StationId
    price: Optional[Decimal]
    departure_time: Optional[datetime]
    arrival_time: Optional[datetime]
    is_booked: bool

    def unbook_ticket(self):
        self.is_booked = False
