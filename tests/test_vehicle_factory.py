from mock import patch, sentinel, Mock
import pytest

from app.vehicle_factory import VehicleFactory


@patch('app.vehicle_factory.random.choice')
def test_create(mock_rnd):
    mock_rnd.return_value = 1
    veh = VehicleFactory.create()
    assert veh.__class__.__name__ == 'Vehicle'
    assert len(veh._operators) == 1
    assert veh._operators[0].__class__.__name__ == 'Solder'