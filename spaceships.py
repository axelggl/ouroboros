from base_spaceships import Spaceship, Battleship, Fighter

class BattleshipKiller:
    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Battleship):
            target_spaceship.take_damages(self.attack * 2)
        else:
            super().fire_on(target_spaceship)

class FighterKiller:
    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Fighter):
            target_spaceship.take_damages(self.attack * 2)
        else:
            super().fire_on(target_spaceship)

class Interceptor(Fighter, FighterKiller):
    attack = 180
    defense = 1000

    def __init__(self):
        super().__init__(self.attack, self.defense)

class Bomber(Fighter, BattleshipKiller):
    attack = 150
    defense = 2000

    def __init__(self):
        super().__init__(self.attack, self.defense)

class Cruiser(Battleship, BattleshipKiller):
    attack = 800
    defense = 3000

    def __init__(self):
        super().__init__(self.attack, self.defense)

class Frigate(Battleship, FighterKiller):
    attack = 500
    defense = 2500

    def __init__(self):
        super().__init__(self.attack, self.defense)

class Destroyer(Battleship, BattleshipKiller):
    attack = 650
    defense = 5000

    def __init__(self):
        super().__init__(self.attack, self.defense)
