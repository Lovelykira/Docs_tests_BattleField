import pytest
from mock import patch, sentinel

from app.squad import Squad
from app.solder import Solder


@pytest.fixture
def fixt_squad():
    squad = Squad()
    squad.add_unit(Solder())
    squad.add_unit(Solder())
    return squad


def test_attack(fixt_squad):
    with patch.object(Solder, 'do_attack') as mock_do_attack:
        mock_do_attack.return_value = 1
        assert fixt_squad.attack() == 2


def test_take_damage(fixt_squad):
    with patch.object(fixt_squad._units[0], 'calc_armor') as mock_calc_armor:
        mock_calc_armor.return_value = 0
        fixt_squad.take_damage(10)
        assert fixt_squad._units[0]._health == 95


def test_is_alive(fixt_squad):
    assert fixt_squad.is_alive() == True
    fixt_squad.take_damage(100000000000000)
    assert fixt_squad.is_alive() == False


def test_get_alive_units(fixt_squad):
    assert fixt_squad.get_alive_units() == fixt_squad._units
    with patch.object(fixt_squad._units[0], 'calc_armor') as mock_calc_armor_0, patch.object(fixt_squad._units[1], 'calc_armor') as mock_calc_armor_1:
        mock_calc_armor_0.return_value = 10000
        mock_calc_armor_1.return_value = 0
        fixt_squad.take_damage(200)
        assert fixt_squad.get_alive_units() == fixt_squad._units[:1]


def test_recharge(fixt_squad):
    assert fixt_squad.recharge() == False
    with patch.object(Solder, 'can_attack') as mock_can_attack:
        mock_can_attack.return_value = False
        assert fixt_squad.recharge() == True


def test_add_unit(fixt_squad):
    fixt_squad.add_unit(sentinel.unit)
    assert fixt_squad._units[-1] == sentinel.unit


