from dataclasses import dataclass
from datetime import date
from typing import Optional

from src.business.domain import entities


@dataclass
class Route:
    id: entities.RouteId
    transport_id: entities.TransportId


@dataclass
class RoutesFromToStationGet:
    from_station_id: int
    to_station_id: int
    offset: int
    limit: int
    departure_date: Optional[date] = None
