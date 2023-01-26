from dataclasses import dataclass

from src.business.domain import entities


@dataclass
class Station:
    id: entities.StationId
    name: str


@dataclass
class StationsGet:
    limit: int
    offset: int
