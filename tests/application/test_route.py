from pytest import raises

from src.business.application.route import dto, exceptions, use_cases
from tests.mocks.db import MockDBGateway


class TestRoute:
    async def test_get_route(
        self, get_route: use_cases.GetRoute, db_gateway: MockDBGateway
    ) -> None:
        db_gateway.clean_db()
        db_gateway.fill_storage()

        with raises(exceptions.RouteNotExists):
            await get_route(-1)

        route = await get_route(1)

        assert route.id == 1

    async def test_get_routes_from_to_station(
        self,
        get_routes_from_to_station: use_cases.GetRoutesFromToStation,
    ) -> None:
        routes = await get_routes_from_to_station(
            dto.RoutesFromToStationGet(1, 2, 0, 10)
        )

        assert len(routes) == 10
