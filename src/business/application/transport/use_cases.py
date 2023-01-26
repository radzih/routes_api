from src.business.application.common import use_cases
from src.business.application.transport import interfaces
from src.business.domain import entities


class GetTransport(use_cases.UseCase):
    def __init__(self, db_gateway: interfaces.DBGateway) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, data: entities.TransportId) -> entities.Transport:
        transport = await self.db_gateway.read_transport(data)
        return transport
