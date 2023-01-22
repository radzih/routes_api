from dataclasses import dataclass
from typing import NewType, Optional

StationId = NewType("StationId", int)


@dataclass
class Station:
    id: Optional[StationId]
    name: str
