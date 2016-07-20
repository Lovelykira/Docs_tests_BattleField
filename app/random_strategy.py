import random

from app.abstract_strategy import AbstractStrategy


class RandomStrategy(AbstractStrategy):
    """
    Class is used to chose the specific squad in army
    """
    @classmethod
    def chose_squad(cls, enemy_army):
        enemy_squad = random.choice(enemy_army.get_alive_squads())
        return enemy_squad
