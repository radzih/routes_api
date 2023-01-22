from pytest import fixture

from src.business.application.user import use_cases
from tests.mocks.db import MockDBGateway


@fixture
def create_user(db_gateway: MockDBGateway) -> use_cases.CreateUser:
    return use_cases.CreateUser(db_gateway)


@fixture
def update_user(db_gateway: MockDBGateway) -> use_cases.UpdateUser:
    return use_cases.UpdateUser(db_gateway)


@fixture
def get_user(db_gateway: MockDBGateway) -> use_cases.GetUser:
    return use_cases.GetUser(db_gateway)
