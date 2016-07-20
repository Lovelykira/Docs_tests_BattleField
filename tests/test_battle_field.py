from mock import patch, sentinel, Mock
import pytest

from app.battle_field import Battlefield
from app.random_strategy import RandomStrategy
from app.army_factory import ArmyFactory
from app.army import Army


@pytest.fixture
def fixt_Bf():
    return Battlefield(2)


def fixt_army():
    return ArmyFactory.create(RandomStrategy)


# @patch('app.battle_field.random.choice')
# def test_start_for(mock_army, fixt_Bf):
#     with patch.object(fixt_Bf._armies[0], 'is_alive') as mock_is_alive:
#         mock_army.return_value = fixt_Bf._armies[1]
#         fixt_Bf.start_for(0, '')

def test_break_condition(fixt_Bf):
    assert fixt_Bf.break_condition() == len(fixt_Bf._armies)


def start(fixt_Bf):
    with patch.object(Army, 'get_strategy') as mock_army_get_strategy, \
            patch.object(fixt_Bf, 'start_for') as mock_start_for, \
            patch.object(fixt_Bf, 'break_condition') as mock_break_cond, \
            patch.object(Army, 'is_alive') as mock_army_is_alive:
        fixt_Bf.start()
        assert mock_army_get_strategy.call_count == len(fixt_Bf._armies)
        assert mock_start_for.call_count == len(fixt_Bf._armies)
        mock_break_cond.called()
        assert mock_army_is_alive.call_cout == len(fixt_Bf._armies)
