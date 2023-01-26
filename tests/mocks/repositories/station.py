from src.business.application.common import interfaces
from src.business.application.station import exceptions
from src.business.domain import entities
from tests.mocks.repositories.base import BaseRepo


class StationReader(interfaces.StationReader, BaseRepo):
    async def read_station(
        self, station_id: entities.StationId
    ) -> entities.Station:
        station = self.storage["station"].get(station_id, None)

        if not station:
            raise exceptions.StationNotExists

        return station

    async def read_stations(
        self, limit: int, offset: int
    ) -> list[entities.Station]:
        stations = list(self.storage["station"].values())[offset:][:limit]
        return stations
