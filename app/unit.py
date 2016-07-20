from abc import ABCMeta, abstractmethod
import random
import time

from app.constants import MAX_UNIT_HEALTH, UNIT_RECHARGE_RANGE, FIRST_ATTACK_TIME


class Unit(metaclass=ABCMeta):
    """
    Abstract Unit class
    """
    def __init__(self):
        self._health = MAX_UNIT_HEALTH
        self._recharge = random.choice(UNIT_RECHARGE_RANGE)
        self._next_attack_time = FIRST_ATTACK_TIME
        self._armor = 0

    @abstractmethod
    def do_attack(self):
        pass

    @abstractmethod
    def take_damage(self, dmg):
        pass

    @abstractmethod
    def calc_armor(self):
        pass

    @abstractmethod
    def get_power(self):
        pass

    def can_attack(self):
        """
        Checks if unit can or can't attack due to recharge.

        :return: True if it can attack, False otherwise.
        """
        now = time.time()
        return now >= self._next_attack_time and self.is_alive()

    def is_alive(self):
        """
        Checks if unit is alive.

        :return: True if it is alive, False otherwise.
        """
        return self._health > 0

    def get_health(self):
        return self._health

    def __str__(self):
        """
        String representation of the object.

        :return: string that is shown when str, print or format are called with unit as parameter.
        :rtype: str.
        """
        return '{} has {} health'.format(self.__class__.__name__,self._health)
