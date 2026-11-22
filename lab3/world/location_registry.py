from ..core.unknown_code_error import UnknownCodeError
from .location import Location
class LocationRegistry:
    def __init__(self, locations: list[Location]):
        self._locations = {loc.code: loc for loc in locations}
    def get(self, code: str) -> Location:
        loc = self._locations.get(code)
        if loc is None: raise UnknownCodeError("Локация", code)
        return loc
    @property
    def all(self) -> list[Location]: return list(self._locations.values())