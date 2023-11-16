from spaceships import Interceptor, Frigate

class Fleet:
    def __init__(self, name, ships):
        self.name = name
        self.ships = ships

class SpaceDock:
    def __init__(self) -> None:
        self.fleets = {'default': Fleet('default', [])}

    def __getitem__(self, key):
        if key not in self.fleets:
            self.fleets[key] = Fleet(key, [])
        return self.fleets[key]

    def __setitem__(self, name, ships):
        if name not in self.fleets:
            self.fleets[name] = Fleet(name, ships)

    def __delitem__(self, name):
        if name in self.fleets:
            del self.fleets[name]

    def __str__(self):
        result = []
        for name, fleet in self.fleets.items():
            result.append(f'{name}: {len(fleet.ships)} ships')
        return ', '.join(result)
