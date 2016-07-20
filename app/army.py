from app.random_strategy import RandomStrategy


class Army:
    """
    Class Army.

    In this class is implemented the attack logic.
    """

    def __init__(self, strategy=RandomStrategy):
        self._squads = []
        self._strategy = strategy

    def get_alive_squads(self):
        """
        Get the list of army's alive squads.

        :return: alive squads.
        :rtype: list.
        """
        alive_squads = []
        for squad in self._squads:
            if squad.is_alive():
                alive_squads.append(squad)
        return alive_squads

    def take_damage(self, squad, dmg):
        """
        Take damage function.

        The damage should be taken by specific squad.
        :param Squad squad: the squad that is attacked.
        :param float dmg: the amount of damage that was dealt.
        """
        squad.take_damage(dmg)

    def attack_for(self, enemy, squad, res):
        res += "<br>&ensp;Attacker's army has {} squad(s) left".format(len(self.get_alive_squads()))
        res += "<br>&ensp;Defender's army has {} squad(s) left<br>".format(len(enemy.get_alive_squads()))
        enemy_squad = self._strategy.chose_squad(enemy_army=enemy)

        res += "<br>Attacker's {}".format(str(squad))
        res += "<br>Defender's {}".format(str(enemy_squad))

        dmg = squad.attack()
        res += "<br>Attacker's dmg = {}".format(dmg)
        enemy.take_damage(enemy_squad, dmg)
        if enemy_squad.is_alive() and not enemy_squad.recharge():
            return_dmg = enemy_squad.attack()
            res += "<br>Defender's dmg = {}<br>".format(return_dmg)
            self.take_damage(squad, return_dmg)
            if not squad.is_alive():
                res += "<br>&ensp;ATTACKER'S SQUAD DIES!"
        elif not enemy_squad.is_alive():
            res += "<br>&ensp;DEFENDER'S SQUAD DIES!\n"
        else:
            res += "<br>Defender is charging"
        return res

    def attack_while(self, enemy):
        if len(self.get_alive_squads()) == 0:
            return  "<br>&ensp;Defender wins"
        if len(enemy.get_alive_squads()) == 0:
            return "<br>&ensp;Attacker wins"
        return ""

    def attack(self, enemy):
        """
        Attack function

        While there are squads in attacker's and defender's Army, the attacker should choose defender's squad according to it's
        strategy. Then attacker's squad damages defender's squad. If defender's squad is alive after that, it strikes back.
        The function returns when there is only one army left.
        :param Army enemy: the defender's Army.
        :return: The return value is used to show log on the screen.
        :rtype: str
        """
        res = ""
        while True:
            if self.attack_while(enemy) != "":
                res += self.attack_while(enemy)
                break

            for squad in self._squads:
                if not squad.is_alive() or squad.recharge():
                    continue
                res += self.attack_for(enemy, squad, res)
        return res

    def add_group(self, group):
        """
        Function that adds group to army.

        At this moment there is only one available group type - Squad.
        :param group: At this moment it is Squad that should be added to army's squads.
        """
        self._squads.append(group)

    def is_alive(self):
        """
        Function that checks if Army is alive.

        :return: True if it's alive, False otherwise.
        """
        if len(self.get_alive_squads()) > 0:
            return True
        else:
            return False

    def get_strategy(self):
        return self._strategy.__name__

    def __str__(self):
        """
        String representation of the object.

        :return: string that is shown when str, print or format are called with Army as parameter.
        :rtype: str.
        """
        squads = self.get_alive_squads()
        squads = '\n'.join([str(squad) for squad in squads])
        return 'Army with {} units: \n{}'.format(len(self.get_alive_squads()), squads)
