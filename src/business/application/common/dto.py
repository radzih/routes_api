from dataclasses import dataclass
from datetime import datetime

from src.business.domain import entities


@dataclass
class RouteStation:
    station_id: entities.StationId
    name: str
    departure_time: datetime
    arrival_time: datetime
