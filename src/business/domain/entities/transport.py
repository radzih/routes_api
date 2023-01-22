from dataclasses import dataclass
from typing import NewType, Optional

TransportId = NewType("TransportId", int)


@dataclass
class Transport:
    id: Optional[TransportId]
    name: str
    capacity: int
