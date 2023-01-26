from datetime import date
from typing import Optional

from src.business.application.common import dto, interfaces
from src.business.application.route import exceptions
from src.business.domain import entities
from tests.mocks.repositories.base import BaseRepo


class RouteReader(interfaces.RouteReader, BaseRepo):
    async def read_route(self, route_id: entities.RouteId) -> entities.Route:
        route = self.storage["route"].get(route_id, None)

        if not route:
            raise exceptions.RouteNotExists

        return route

    async def read_routes_from_to_station(
        self,
        limit: int,
        offset: int,
        to_station_id: entities.StationId,
        from_station_id: entities.StationId,
        departure_date: Optional[date] = None,
    ) -> list[entities.Route]:
        routes = list(self.storage["route"].values())

        if all(
            (
                from_station_id == 1,
                to_station_id == 2,
            )
        ):
            return routes[offset:][:limit]

        return []

    async def read_route_stations(
        self, route_id: entities.RouteId
    ) -> list[dto.RouteStation]:
        route = self.storage["route"].get(route_id, None)

        if not route:
            raise exceptions.RouteNotExists

        route_stations = list(self.storage["route_station"].values())

        stations = [
            station for station in route_stations if station.id == route_id
        ]

        return stations
