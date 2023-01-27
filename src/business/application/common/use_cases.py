from typing import Protocol, TypeVar

InputDTO = TypeVar("InputDTO")
OutputDTO = TypeVar("OutputDTO")


class UseCase(Protocol):
    async def __call__(self, data):
        raise NotImplementedError
