from pytest import raises

from src.business.application.transport import exceptions, use_cases
from tests.mocks.db import MockDBGateway


class TestTransport:
    async def test_get_transport(
        self, get_transport: use_cases.GetTransport, db_gateway: MockDBGateway
    ) -> None:
        db_gateway.clean_db()
        db_gateway.fill_storage()

        transport = await get_transport(1)

        assert transport.id == 1
        assert transport.name == "Merc"
        assert transport.capacity == 20

        with raises(exceptions.TransportNotExists):
            await get_transport(-1)
