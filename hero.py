from character import Character
from termcolor import colored
from dungeon import Dungeon


class Hero(Character):

    def __init__(self, name="Bron", title="Dragonslayer",
                 health=100, mana=100, mana_regeneration_rate=2):
        super(Hero, self).__init__(health, mana)
        self.__max_mana = mana
        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def take_mana(self, mana_points):
        if mana_points > self.__max_mana:
            self.__mana = self.__max_mana
        else:
            self.__mana += mana_points + self.__mana_regeneration_rate

    def attack(self, by):
        if by == "weapon":
            print(colored(self.known_as(), "green", attrs=['bold']),
                  "is attacking with", colored(str(self.get_weapon()), "cyan",
                                               attrs=['bold']), "for",
                  colored(int(self.get_weapon()),
                          "red", attrs=['bold']), "dmg")
            return int(self.get_weapon())
        elif by == "spell":
            if self.__spell_attack() is False:
                print(colored(self.known_as(), 'green', attrs=['bold']),
                      "does not have enough",
                      colored("mana", 'blue', attrs=['bold']), "for another",
                      colored(self.get_spell().get_name(), "yellow",
                              attrs=['bold']))
                return self.attack("weapon")
            else:
                print(colored(self.known_as(), "green", attrs=['bold']),
                      "is attacking with",
                      colored(self.get_spell().get_name(), "yellow",
                              attrs=['bold']), "for",
                      colored(self.get_spell().get_damage(), "red",
                              attrs=['bold']), "dmg")
                return self.get_spell().get_damage()
        else:
            raise Exception("Illegal attack method")

    def __spell_attack(self):
        if self.get_mana() >= self.get_spell().get_mana_cost():
            self.lower_mana(self.get_spell().get_mana_cost())
            return self.get_spell().get_damage()
        else:
            return False
