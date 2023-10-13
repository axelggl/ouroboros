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
    attack = 180
    defense = 1000

class Bomber(Fighter, BattleshipKiller):
    attack = 150
    defense = 2000

class Cruiser(Battleship, BattleshipKiller):
    attack = 800
    defense = 3000

class Frigate(Battleship, FighterKiller):
    attack = 500
    defense = 2500

class Destroyer(Battleship, BattleshipKiller):
    attack = 650
    defense = 5000

