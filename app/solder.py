import time
import random

from app.unit import Unit
from app.constants import START_SOLDER_EXPERIENCE, MAX_SOLDER_EXPERIENCE


class Solder(Unit):
    def __init__(self):
        super().__init__()
        self._experience = START_SOLDER_EXPERIENCE

    def do_attack(self):
        """
        Attack func.

        Calculates the attack power of the soldier, increases it's experience, sets the recharge.
        :return: result of get_power.
        """
        self._next_attack_time = time.time() + self._recharge
        if self._experience != MAX_SOLDER_EXPERIENCE:
            self._experience += 1

        return self.get_power()

    def take_damage(self, dmg):
        """
        Reduces the health of Solder.

        :param float dmg: the amount of damage to take.
        """
        self._armor = self.calc_armor()
        if self._armor < dmg:
            self._health = self._health - dmg + self._armor

    def calc_armor(self):
        """
        Calculate the armor.

        :return: the amount of armor to reduce the damage.
        :rtype: float.
        """
        return 0.05 + self._experience / 100

    def get_experience(self):
        """
        Returns the value of experience.

        :return: solder's experience.
        :rtype: int.
        """
        return self._experience

    def get_power(self):
        """
        Calculate the power of the solder.

        :return: attack power.
        :rtype: float.
        """
        return 0.5 * (1 + self._health) * random.randint(50 + self._experience, 100) / 100
