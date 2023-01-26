from src.business.application.common import interfaces
from src.business.application.transport import exceptions
from src.business.domain import entities
from tests.mocks.repositories import BaseRepo


class TransportReader(interfaces.TransportReader, BaseRepo):
    async def read_transport(
        self, transport_id: entities.TransportId
    ) -> entities.Transport:
        transport = self.storage["transport"].get(transport_id, None)

        if not transport:
            raise exceptions.TransportNotExists

        return transport
