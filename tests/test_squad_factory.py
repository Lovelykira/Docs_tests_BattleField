import pytest
from mock import patch

from app.squad_factory import SquadFactory

@patch('app.squad_factory.random.choice')
def test_create(mock_rnd_choice):
    mock_rnd_choice.return_value = 1
    squad = SquadFactory.create()
    assert squad.__class__.__name__ == 'Squad'
    assert len(squad._units) == 2
    assert (squad._units[0].__class__.__name__ == 'Solder' and squad._units[1].__class__.__name__ == 'Vehicle'
            or squad._units[1].__class__.__name__ == 'Solder' and squad._units[0].__class__.__name__ == 'Vehicle')
