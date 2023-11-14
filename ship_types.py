from enum import Enum
from spaceships import Interceptor, Bomber, Cruiser, Frigate, Destroyer

class ShipType(Enum):
    INTERCEPTOR = Interceptor
    BOMBER = Bomber
    CRUISER = Cruiser
    FRIGATE = Frigate
    DESTROYER = Destroyer