import random

from app.vehicle import Vehicle
from app.solder_factory import SolderFactory
from app.constants import NUM_OPERATORS_RANGE


class VehicleFactory:
    """
    Class that creates Vehicle objects.
    """
    @classmethod
    def create(cls):
        """
        Create Vehicle.

        Creates Vehicle object with random number of operators.
        :return: Vehicle object.
        """
        vehicle = Vehicle()
        num_operators = random.choice(NUM_OPERATORS_RANGE)
        for i in range(num_operators):
            vehicle.add_operator((SolderFactory.create()))
        return vehicle