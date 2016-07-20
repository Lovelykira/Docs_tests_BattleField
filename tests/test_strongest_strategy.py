from mock import patch, sentinel, Mock
import pytest

from app.army import Army
from app.squad import Squad
from app.solder import Solder
from app.strongest_strategy import StrongestStrategy


@pytest.fixture
def fixt_army():
    army = Army(StrongestStrategy)
    squad1 = Squad()
    squad1.add_unit(Solder())
    squad1.add_unit(Solder())
    squad1.add_unit(Solder())
    squad1.add_unit(Solder())
    squad1.add_unit(Solder())
    squad2 = Squad()
    squad2.add_unit(Solder())
    army.add_group(squad1)
    army.add_group(squad2)
    return army


def test_strongest_strategy(fixt_army):
    assert fixt_army._strategy.chose_squad(fixt_army) == fixt_army._squads[1]
