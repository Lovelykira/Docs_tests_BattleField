from mock import patch, sentinel, Mock
import pytest
import random

from app.army_factory import ArmyFactory
from app.squad_factory import SquadFactory
from app.squad import Squad
from app.solder import Solder
from app.constants import STRATEGIES


@pytest.fixture
def fixt_dead_squad():
    squad = Squad()
    solder = Solder()
    solder._health = 0
    squad.add_unit(solder)
    return squad


@pytest.fixture
def fixt_squad():
    squad = SquadFactory.create()
    return squad


@pytest.fixture
def fixt_army():
    army = ArmyFactory.create(STRATEGIES[0])
    return army

@pytest.fixture
def fixt_enemy_army():
    army = ArmyFactory.create(STRATEGIES[0])
    return army


def test_get_alive_squads(fixt_army, fixt_dead_squad):
    assert fixt_army.get_alive_squads() == fixt_army._squads
    fixt_army.add_group(fixt_dead_squad)
    assert len(fixt_army.get_alive_squads()) == len(fixt_army._squads) - 1


def test_take_damage(fixt_army):
    with patch.object(fixt_army._squads[0], 'take_damage') as mock_squad_take_damage:
        fixt_army.take_damage(fixt_army._squads[0], sentinel.dmg)
        mock_squad_take_damage.assert_called_once_with(sentinel.dmg)


def test_attack_for( fixt_army, fixt_enemy_army, fixt_squad):

    with patch.object(fixt_army._strategy, 'chose_squad', return_value=fixt_squad) as mock_chose_squad, \
            patch.object(fixt_army._squads[0], 'attack') as mock_squad_attack, \
            patch.object(fixt_enemy_army, 'take_damage') as mock_enemy_take_dmg, \
            patch.object(fixt_army, 'take_damage') as mock_take_dmg, \
            patch.object(fixt_army._squads[0], 'is_alive') as mock_squad_is_alive:
                    #patch.object(mock_chose_squad(), 'attack') as mock_enemy_attack


        fixt_army.attack_for(fixt_enemy_army, fixt_army._squads[0], '')
        mock_chose_squad.assert_called_once_with(enemy_army=fixt_enemy_army)
        mock_squad_attack.assert_called_once()
        mock_enemy_take_dmg.assert_called_once()
        mock_take_dmg.assert_called_once()
        mock_squad_is_alive.assert_called()
       # mock_enemy_attack.assert_called_once()


def test_attack_while(fixt_army, fixt_enemy_army):
    assert fixt_army.attack_while(fixt_enemy_army) == ""

    with patch.object(fixt_army, 'get_alive_squads', return_value=[]):
        assert fixt_army.attack_while(fixt_enemy_army) == "<br>&ensp;Defender wins"

    with patch.object(fixt_enemy_army, 'get_alive_squads', return_value=[]):
        assert fixt_army.attack_while(fixt_enemy_army) == "<br>&ensp;Attacker wins"


def attack(fixt_army, fixt_enemy_army):
    with patch.object(fixt_army, 'attack_while') as mock_self_attack_while, \
            patch.object(fixt_army, 'attack_for') as mock_self_attack_for:
        fixt_army.attack(fixt_enemy_army)
        mock_self_attack_while.called()
        assert mock_self_attack_for.call_count() == fixt_army._squads


def test_add_group(fixt_army, fixt_squad):
    army_len = len(fixt_army.get_alive_squads())
    fixt_army.add_group(fixt_squad)
    assert len(fixt_army.get_alive_squads()) == army_len + 1


def test_get_strategy(fixt_army):
    assert fixt_army.get_strategy() == STRATEGIES[0].__name__

