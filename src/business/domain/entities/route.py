from dataclasses import dataclass
from typing import NewType, Optional

from .transport import TransportId

RouteId = NewType("RouteId", int)


@dataclass
class Route:
    id: Optional[RouteId]
    transport_id: TransportId
