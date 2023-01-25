from datetime import datetime, timedelta

from src.business.domain import entities
from tests.mocks import repositories

TABLES = [
    "ticket",
    "user",
]


class MockDBGateway(
    repositories.UserSaver,
    repositories.UserReader,
    repositories.TicketReader,
    repositories.TicketRemover,
    repositories.TicketSaver,
    repositories.Commiter,
):
    def __init__(self) -> None:
        self.storage = {}
        self.to_commit = {}

        for table in TABLES:
            self.storage.update({table: {}})
            self.to_commit.update({table: {}})

    def fill_storage(self):
        for i in range(1, 11):
            self.storage["user"][i] = entities.User(
                id=i,
                name=f"User{i}",
                surname=f"Surname{i}",
                email=f"{i}mail@mail.com",
            )

        for booked in (True, False):
            for i in range(1, 21):
                self.storage["ticket"][i] = entities.Ticket(
                    id=i,
                    route_id=1,
                    user_id=(i - 1) // 2 + 1,
                    from_station_id=i,
                    to_station_id=i + 1,
                    price=100,
                    departure_time=datetime.now(),
                    arrival_time=datetime.now() + timedelta(hours=1),
                    is_booked=booked,
                )

    def clean_db(self):
        self.__init__()
