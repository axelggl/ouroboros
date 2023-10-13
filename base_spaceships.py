class Spaceship:
    is_alive = True

    def __init__(self, attack=0, defense=0):
        self.attack = attack
        self.defense = defense

    def take_damages(self, damage):
        """
        Apply damage to the spaceship's defense.

        :param damage: The amount of damage to apply.
        :type damage: int

        :raises ValueError: If damage is negative.
        """
        if damage < 0:
            raise ValueError("Damage cannot be negative.")

        self.defense -= damage
        if self.defense <= 0:
            self.defense = 0
            self.is_alive = False
            
    def fire_on(self, target_spaceship):
        """
        Apply damage to the target spaceship based on the attacker's attack attribute.

        :param target_spaceship: The spaceship to be targeted.
        :type target_spaceship: Spaceship
        """
        target_spaceship.take_damages(self.attack)
        

class Battleship(Spaceship):
    def __init__(self, attack=0, defense=0):
        super().__init__(attack, defense)

class Fighter(Spaceship):
    def __init__(self, attack=0, defense=0):
        super().__init__(attack, defense)