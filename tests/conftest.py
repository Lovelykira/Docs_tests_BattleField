import pytest

from app.abstract_strategy import AbstractStrategy

@pytest.fixture
def fixt_test_strategy():
    class TestStrategy(AbstractStrategy):
        @classmethod
        def chose_squad(cls, enemy_army):
            for squad in enemy_army.get_alive_squads():
                return squad