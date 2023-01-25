class BaseRepo:
    def __init__(self) -> None:
        self.storage = {}
        self.to_commit = {}


class Commiter(BaseRepo):
    async def commit(self) -> None:
        for table in self.storage:
            self.storage[table].update(self.to_commit[table])
