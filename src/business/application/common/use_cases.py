from typing import TypeVar, Protocol

InputDTO = TypeVar("InputDTO")
OutputDTO = TypeVar("OutputDTO")


class UseCase(Protocol):
    def __call__(self, data: InputDTO) -> OutputDTO:
        raise NotImplementedError
