import random
import time

from app.unit import Unit


class Vehicle(Unit):
    def __init__(self):
        super().__init__()
        self._operators = []

    def do_attack(self):
        """
        Attack func

        Calculates the attack power of the vehicle, sets the recharge
        :return: result of get_power
        """
        self._next_attack_time = time.time() + self._recharge
        return self.get_power()

    def take_damage(self, dmg):
        """
        Reduces the health of vehicle and the healths of it's operator's.

        Vehicle takes 60% of damage, one operator takes 20%, the other ones - 10%.
        :param float dmg: damage that shoul be taken be vehicle.
        """
        veh_dmg = dmg * 0.6
        self._armor = self.calc_armor()
        if self._armor < veh_dmg:
            self._health = self._health - veh_dmg + self._armor
        random_operator_dmg = dmg * 0.2
        random_operator = random.choice(self._operators)
        random_operator.take_damage(random_operator_dmg)
        died = True
        for operator in self._operators:
            if operator != random_operator:
                operator.take_damage(dmg * 0.1)
            if operator.is_alive():
                died = False
        if died:
            self._health = 0


    def calc_armor(self):
        """
        Calculate the armor.

        :return: the amount of armor to reduce the damage.
        :rtype: float.
        """
        operators_sum_exp = 0
        for operator in self._operators:
            operators_sum_exp += operator.get_experience() / 100
        return 0.1 + operators_sum_exp

    def add_operator(self, operator):
        """
        Function that adds operator to vehicle.

        :param operator: At this moment operator can only be Solder object.
        """
        self._operators.append(operator)

    def get_power(self):
        """
        Calculate the power of the vehicle.

        :return: attack power.
        :rtype: float.
        """
        op_sum_attack = 0
        for operator in self._operators:
            op_sum_attack += operator.do_attack()
        return 0.5 * (1 + self._health / 100) * op_sum_attack / len(self._operators)
