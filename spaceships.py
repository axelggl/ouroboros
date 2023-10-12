from base_spaceships import Spaceship, Battleship, Fighter

class Interceptor(Fighter):
    attack = 180
    defense = 1000

    def __init__(self):
        super().__init__(self.attack, self.defense)

    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Fighter):
            target_spaceship.take_damages(self.attack * 2)
        else:
            super().fire_on(target_spaceship)

class Bomber(Fighter):
    attack = 150
    defense = 2000

    def __init__(self):
        super().__init__(self.attack, self.defense)

    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Battleship):
            target_spaceship.take_damages(self.attack * 2)
        else:
            super().fire_on(target_spaceship)

class Cruiser(Battleship):
    attack = 800
    defense = 3000

    def __init__(self):
        super().__init__(self.attack, self.defense)

class Frigate(Battleship):
    attack = 500
    defense = 2500

    def __init__(self):
        super().__init__(self.attack, self.defense)

    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Fighter):
            target_spaceship.take_damages(self.attack * 2)
        else:
            super().fire_on(target_spaceship)

class Destroyer(Battleship):
    attack = 650
    defense = 5000

    def __init__(self):
        super().__init__(self.attack, self.defense)

    def fire_on(self, target_spaceship):
        if isinstance(target_spaceship, Battleship):
            target_spaceship.take_damages(self.attack * 2)
        else:
            super().fire_on(target_spaceship)