class Squad:
    def __init__(self):
        self._units = []

    def attack(self):
        """
        Calculates the attack power of squad.

        :return: attack power.
        :rtype: float.
        """
        power = 0
        for unit in self._units:
            if unit.can_attack():
                power += unit.do_attack()
        return power

    def take_damage(self, dmg):
        """
        The damage that is dealt to squad is spread evenly among it's units

        :param float dmg: the damage that should be taken by squad.
        """
        num_alive_units = len(self.get_alive_units())
        dmg_per_alive_unit = dmg / num_alive_units
        for unit in self.get_alive_units():
            unit.take_damage(dmg_per_alive_unit)

    def is_alive(self):
        """
        Function that checks if Squad is alive.

        :return: True if it's alive, False otherwise.
        """
        for unit in self._units:
            if unit.is_alive():
                return True
        return False

    def get_alive_units(self):
        """
        Get the list of squad's alive units.

        :return: alive units.
        :rtype: list.
        """
        alive_units = []
        for unit in self._units:
            if unit.is_alive():
                alive_units.append(unit)
        return alive_units

    def recharge(self):
        """
        Checks if squad can or can't attack due to recharge.

        :return: True if it's recharging, False otherwise.
        """
        for unit in self._units:
            if unit.can_attack():
                return False
        else:
            return True

    def add_unit(self, unit):
        """
        Function that adds unit to squad.

        At this moment there are two available unit types - Solder and Vehicle.
        :param unit: Solder or Vehicle that should be added to squad's units.
        """
        self._units.append(unit)

    def __str__(self):
        """
        String representation of the object.

        :return: string that is shown when str, print or format are called with Squad as parameter.
        :rtype: str.
        """
        units = self.get_alive_units()
        units = '\n'.join([str(unit) for unit in units])
        return 'Squad with {} units: \n{}'.format(len(self.get_alive_units()), units)

