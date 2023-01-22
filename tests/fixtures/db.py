from pytest import fixture

from tests.mocks.db import MockDBGateway


@fixture(scope="session")
def db_gateway():
    return MockDBGateway()
