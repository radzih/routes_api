from dataclasses import dataclass
from typing import Optional

from src.business.domain import entities


@dataclass
class UserCreate:
    name: str
    surname: str
    email: str


@dataclass
class UserUpdate:
    id: entities.UserId
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]


@dataclass
class User:
    id: entities.UserId
    name: str
    surname: str
    email: str
