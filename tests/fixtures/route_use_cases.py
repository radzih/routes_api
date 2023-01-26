from pytest import fixture

from src.business.application.route import use_cases
from tests.mocks.db import MockDBGateway


@fixture
def get_route(db_gateway: MockDBGateway) -> use_cases.GetRoute:
    return use_cases.GetRoute(db_gateway)


@fixture
def get_route_stations(
    db_gateway: MockDBGateway,
) -> use_cases.GetRouteStations:
    return use_cases.GetRouteStations(db_gateway)


@fixture
def get_routes_from_to_station(
    db_gateway: MockDBGateway,
) -> use_cases.GetRoutesFromToStation:
    return use_cases.GetRoutesFromToStation(db_gateway)
