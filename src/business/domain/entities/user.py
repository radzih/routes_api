from dataclasses import dataclass
from typing import NewType, Optional

UserId = NewType("UserId", int)


@dataclass
class User:
    id: Optional[UserId]
    name: str
    surname: str
    email: str
