from src.business.application.common.interfaces import (
    Commiter,
    UserReader,
    UserSaver,
)


class DBGateway(UserSaver, UserReader, Commiter):
    pass
