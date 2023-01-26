from dataclasses import asdict

from src.business.application.common import use_cases
from src.business.application.station import dto, interfaces
from src.business.domain import entities


class GetStation(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.StationId) -> dto.Station:
        station = await self.db_gateway.read_station(data)
        return dto.Station(**asdict(station))


class GetStations(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.StationsGet) -> dto.Station:
        stations = await self.db_gateway.read_stations(data.limit, data.offset)
        return [dto.Station(**asdict(station)) for station in stations]
