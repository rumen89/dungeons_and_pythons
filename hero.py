from character import Character


class Hero(Character):

    def __init__(self, name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2):
        super(Hero, self).__init__(health, mana)
        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def take_mana(self, mana_points):
        if mana_points > self.__max_mana:
            self.__mana = self.__max_mana
        else:
            self.__mana += mana_points + 2

    def atack(self, by):
        pass
