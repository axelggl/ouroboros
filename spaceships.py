from base_spaceships import Spaceship, Battleship, Fighter

class BattleshipKiller:
    def __init__(self):
        self.attack = 0
        self.defense = 0

    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Battleship):
            target_spaceship.take_damages(self.attack * 2)

class FighterKiller:
    def __init__(self):
        self.attack = 0
        self.defense = 0

    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Fighter):
            target_spaceship.take_damages(self.attack * 2)

class Interceptor(Fighter, FighterKiller):
    def __init__(self, attack=180, defense=1000):
        super().__init__(attack, defense)

class Bomber(Fighter, BattleshipKiller):
    def __init__(self, attack=150, defense=2000):
        super().__init__(attack, defense)

class Cruiser(Battleship, BattleshipKiller):
    def __init__(self, attack=800, defense=3000):
        super().__init__(attack, defense)

class Frigate(Battleship, FighterKiller):
    def __init__(self, attack=500, defense=2500):
        super().__init__(attack, defense)

class Destroyer(Battleship, BattleshipKiller):
    def __init__(self, attack=650, defense=5000):
        super().__init__(attack, defense)
