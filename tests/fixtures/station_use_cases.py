from pytest import fixture

from src.business.application.station import use_cases
from tests.mocks.db import MockDBGateway


@fixture
def get_station(db_gateway: MockDBGateway) -> use_cases.GetStation:
    return use_cases.GetStation(db_gateway)


@fixture
def get_stations(db_gateway: MockDBGateway) -> use_cases.GetStations:
    return use_cases.GetStations(db_gateway)
