from mock import patch, sentinel, Mock
import pytest

from app.random_strategy import RandomStrategy
from app.army_factory import ArmyFactory
from app.squad import Squad


@pytest.fixture
def fixt_army():
    army = ArmyFactory.create(RandomStrategy)
    return army

@pytest.fixture
def fixt_enemy_army():
    army = ArmyFactory.create(RandomStrategy)
    return army

def fixt_squad():
    return Squad()


@patch('app.random_strategy.random.choice', return_value=fixt_squad)
def test_random_strategy(mock_choice,fixt_army, fixt_enemy_army):
    rnd_squad = fixt_army._strategy.chose_squad(fixt_enemy_army)
    assert rnd_squad == fixt_squad