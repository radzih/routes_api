from src.business.application.common import interfaces


class DBGateway(
    interfaces.Commiter,
    interfaces.TicketReader,
    interfaces.TicketSaver,
    interfaces.TicketRemover,
    interfaces.UserReader,
):
    pass
