from pytest import fixture

from src.business.application.transport import use_cases
from tests.mocks.db import MockDBGateway


@fixture
def get_transport(db_gateway: MockDBGateway) -> use_cases.GetTransport:
    return use_cases.GetTransport(db_gateway)
