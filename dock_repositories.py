import pickle
from dock import SpaceDock

class SpaceDockFileRepository:
    def __init__(self, name: str) -> None:
        self.name = name

    def save(self, dock: SpaceDock) -> None:
        with open(self.name, 'wb') as file:
            pickle.dump(dock, file)

    def load(self) -> SpaceDock:
        try:
            with open(self.name, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return SpaceDock()

