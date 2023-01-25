from src.business.application.common import exceptions


class TicketNotExists(exceptions.ApplicationException):
    pass


class InvalidTicketCreateData(exceptions.ApplicationException):
    pass
