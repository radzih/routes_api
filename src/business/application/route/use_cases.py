from dataclasses import asdict
from operator import attrgetter

from src.business.application.common import use_cases
from src.business.application.common.dto import RouteStation
from src.business.application.route import dto, interfaces
from src.business.domain import entities


class GetRoute(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.RouteId) -> dto.Route:
        route = await self.db_gateway.read_route(data)

        return dto.Route(**asdict(route))


class GetRoutesFromToStation(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(
        self, data: dto.RoutesFromToStationGet
    ) -> list[dto.Route]:
        routes = await self.db_gateway.read_routes_from_to_station(
            **asdict(data)
        )

        return [dto.Route(**asdict(route)) for route in routes]


class GetRouteStations(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.RouteId) -> list[RouteStation]:
        route_stations = await self.db_gateway.read_route_stations(data)

        route_stations.sort(key=attrgetter("departure_time"))
        return [RouteStation(**asdict(station)) for station in route_stations]
