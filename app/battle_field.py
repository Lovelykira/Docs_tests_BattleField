import random

from app.army_factory import ArmyFactory
from app.constants import STRATEGIES


class Battlefield:
    """
    Class that implements armies' battle logic.
    """
    def __init__(self, num_armies):
        self._armies = []
        for i in range(num_armies):
            self._armies.append(ArmyFactory.create(random.choice(STRATEGIES)))

    def start_for(self, i, res):
        if self._armies[i].is_alive() and len([x for x in self._armies if x.is_alive()]) > 1:
            target_army = random.choice([x for x in self._armies if x != self._armies[i] and x.is_alive()])
            res += "<br><br>&ensp;NEW BATTLE army # {} ATTACKS army # {}. It's strategy is {}<br>".format(i, self._armies.index(target_army), self._armies[i].get_strategy())
            res += self._armies[i].attack(target_army)
        return res

    def break_condition(self):
        return len([x for x in self._armies if x.is_alive()])

    def start(self):
        """
        The function that starts the war.

        While there are more than two armies on battlefield, one army should attack the other. The armies' selection is random.
        :return::return: The return value is used to show log on the screen.
        :rtype: str
        """
        res = ""
        res += "There are {} armies.<br> The strategies are:".format(len(self._armies))
        for i in range(0, len(self._armies)):
            res += "<br>{} - {}".format(i, self._armies[i].get_strategy())
        while True:
            for i in range(0, len(self._armies)):
                res = self.start_for(i, res)

            if self.break_condition()==1:
                break

        for i in range(0, len(self._armies)):
            if self._armies[i].is_alive():
                res += "<br><br>&ensp;ARMY # {} WINS THE WAR. {} IS THE BEST".format(i, self._armies[i].get_strategy())

        return res



