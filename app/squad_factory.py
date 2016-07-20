import random

from app.solder_factory import SolderFactory
from app.vehicle_factory import VehicleFactory
from app.squad import Squad
from app.constants import NUM_SOLDERS_RANGE, NUM_VEHICLE_RANGE


class SquadFactory:
    """
    Class that creates Squad objects.
    """
    _available_units = {SolderFactory: NUM_SOLDERS_RANGE, VehicleFactory: NUM_VEHICLE_RANGE}

    @classmethod
    def create(cls):
        """
        Create Squad.

        Creates Squad object with random number of units.
        :return: Squad object.
        """
        squad = Squad()
        factories = cls._available_units
        for factory, number in factories.items():
            for i in range(random.choice(number)):
                squad.add_unit(factory.create())
        return squad