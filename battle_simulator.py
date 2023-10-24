from base_spaceships import Spaceship
import random

class Simulator:
  @staticmethod
  def _duel_fight(attacker_ship: Spaceship, defender_ship: Spaceship):
    attacker_ship.fire_on(defender_ship)

    if defender_ship.is_alive == True:
      defender_ship.fire_on(attacker_ship)

  def _simulate_fight(self, attacker_ships, defender_ships):
        if not len(attacker_ships) or not len(defender_ships):
            pass
        else:
            for attacker in attacker_ships:
                alive_defenders = [defender for defender in defender_ships if defender.is_alive]
                if alive_defenders:
                    defender_ship = random.choice(alive_defenders)
                    self._duel_fight(attacker, defender_ship)