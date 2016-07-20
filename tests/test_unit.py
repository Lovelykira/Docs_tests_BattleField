import pytest
from mock import patch
import time

from app.solder import Solder


@pytest.fixture
def fixt_unit():
    return Solder()


def test_can_attack(fixt_unit):
    assert fixt_unit.can_attack() == True
    fixt_unit._next_attack_time = time.time() + 5
    assert fixt_unit.can_attack() == False


def test_is_alive(fixt_unit):
    assert fixt_unit.is_alive() == True
    fixt_unit._health = -1
    assert fixt_unit.is_alive() == False


def test_get_health(fixt_unit):
    assert fixt_unit.get_health() == 100
    fixt_unit._health = 5
    assert fixt_unit.get_health() == 5




