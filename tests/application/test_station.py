from pytest import raises

from src.business.application.station import dto, exceptions, use_cases
from tests.mocks.db import MockDBGateway


class TestStation:
    async def test_get_station(
        self, get_station: use_cases.GetStation, db_gateway: MockDBGateway
    ) -> None:
        db_gateway.clean_db()
        db_gateway.fill_storage()

        station = await get_station(1)

        assert station.id == 1
        assert station.name == "Station1"

        with raises(exceptions.StationNotExists):
            await get_station(-1)

    async def test_get_stations(
        self, get_stations: use_cases.GetStations
    ) -> None:
        stations = await get_stations(dto.StationsGet(10, 0))

        assert len(stations) == 10

        stations = await get_stations(dto.StationsGet(10, 5))

        assert len(stations) == 5
