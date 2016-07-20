from mock import patch, sentinel, Mock
import pytest

from app.vehicle_factory import VehicleFactory
from app.solder import Solder


@pytest.fixture
def fixt_vehicle():
    return VehicleFactory.create()


def test_do_attack(fixt_vehicle):
    with patch.object(fixt_vehicle, 'get_power') as mock_get_power:
        mock_get_power.return_value = sentinel.get_power
        assert fixt_vehicle.do_attack() == sentinel.get_power


def test_take_damage(fixt_vehicle):
    with patch.object(Solder, 'take_damage') as mock_take_dmg:
        fixt_vehicle.take_damage(10)
        assert mock_take_dmg.call_count == len(fixt_vehicle._operators)

    fixt_vehicle.take_damage(float('inf'))
    assert fixt_vehicle._health == 0
