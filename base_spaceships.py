class Spaceship:
    is_alive = True

    def __init__(self, attack=0, defense=0):
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        if damage < 0:
            raise ValueError("Damage cannot be negative.")
        self.defense -= damage
        if self.defense <= 0:
            self.defense = 0
            self.is_alive = False