import random

from app.squad_factory import SquadFactory
from app.army import Army
from app.constants import NUM_SQUADS_RANGE


class ArmyFactory:
    """
    Class that creates Army objects.
    """
    __available_groups = {SquadFactory: NUM_SQUADS_RANGE}

    @classmethod
    def create(cls, strategy):
        """
        Create Army.

        Creates Army object with specific strategy that is passed as parameter.
        :param strategy: the strategy that should use Army to choose squad to attack.
        :return: Army object.
        """
        army = Army(strategy)
        for factory, number in cls.__available_groups.items():
            for i in range(random.choice(number)):
                army.add_group(factory.create())
        return army