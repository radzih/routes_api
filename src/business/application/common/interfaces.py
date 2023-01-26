from datetime import date
from typing import Optional, Protocol

from src.business.application.common import dto
from src.business.domain import entities


class Commiter(Protocol):
    async def commit(self) -> None:
        ...


class UserReader(Protocol):
    async def read_user(self, user_id: entities.UserId) -> entities.User:
        ...


class UserSaver(Protocol):
    async def save_user(self, user: entities.User) -> entities.UserId:
        ...


class TicketReader(Protocol):
    async def read_user_tickets(
        self,
        user_id: entities.UserId,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
    ) -> list[entities.Ticket]:
        ...

    async def read_ticket(
        self,
        ticket_id: entities.TicketId,
    ) -> entities.Ticket:
        ...


class TicketSaver(Protocol):
    async def save_ticket(self, ticket: entities.Ticket) -> entities.TicketId:
        ...


class TicketRemover(Protocol):
    async def remove_ticket(self, ticket_id: entities.TicketId) -> None:
        ...


class StationReader(Protocol):
    async def read_station(
        self, station_id: entities.StationId
    ) -> entities.Station:
        ...

    async def read_stations(
        self, limit: int, offset: int
    ) -> list[entities.Station]:
        ...


class RouteReader(Protocol):
    async def read_route(self, route_id: entities.RouteId) -> entities.Route:
        ...

    async def read_routes_from_to_station(
        self,
        limit: int,
        offset: int,
        to_station_id: entities.StationId,
        from_station_id: entities.StationId,
        departure_date: Optional[date] = None,
    ) -> list[entities.Route]:
        ...

    async def read_route_stations(
        self,
        route_id: entities.RouteId,
    ) -> list[dto.RouteStation]:
        ...


class TransportReader(Protocol):
    async def read_transport(
        self, transport_id: entities.TransportId
    ) -> entities.Transport:
        ...
