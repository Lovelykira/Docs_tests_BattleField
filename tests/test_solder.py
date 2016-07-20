from mock import patch, sentinel, Mock
import pytest

from app.solder_factory import SolderFactory


@pytest.fixture
def fixt_solder():
    return SolderFactory.create()


def test_do_attack(fixt_solder):
    with patch.object(fixt_solder, 'get_power') as mock_get_power:
        mock_get_power.return_value = sentinel.get_power
        assert fixt_solder.do_attack() == sentinel.get_power


def test_take_dmg(fixt_solder):
    with patch.object(fixt_solder, 'calc_armor') as mock_calc_armor:
        mock_calc_armor.return_value = 0
        fixt_solder.take_damage(10)
        assert fixt_solder._health == 90


def test_calc_armor(fixt_solder):
    fixt_solder._experience = 2
    assert fixt_solder.calc_armor() == 0.07


def test_get_exp(fixt_solder):
    fixt_solder._experience = 5
    assert fixt_solder.get_experience() == 5


@patch('app.solder.random.randint')
def test_get_power(mock_rnd,fixt_solder):
    mock_rnd.return_value = 5
    fixt_solder._health = 100
    assert fixt_solder.get_power() == 2.525