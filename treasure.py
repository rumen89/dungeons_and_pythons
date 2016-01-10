import json
import random
from spell import Spell
from weapon import Weapon


class Treasure:

    def __init__(self):
        ran = self.__random_value()
        self.__treasure_type = None
        self.__treasure = self.__get_random_treasure(ran)

    def get_treasure_type(self):
        return self.__treasure_type


    def loot_treasure(self):
        return self.__treasure

    def __random_value(self):
        return random.randint(0, 3)

    def __random_treasure_type(self, treasures, value):
        key = treasures['treasures'][value].keys()
        for k in key:
            return k

    def __get_random_treasure(self, value):
        treasure_file = open('treasures.json', "r")
        treasures = json.load(treasure_file)
        self.__treasure_type = self.__random_treasure_type(treasures, value)

        ran = random.randint(0, len(treasures['treasures'][
                             value][self.__treasure_type]) - 1)
        return self.__create_treasure(self.__treasure_type, treasures, ran, value)

    def __create_treasure(self, type, treasures, ran, value):
        if type == "mana":
            return treasures['treasures'][value][self.__treasure_type][ran]['mp']
        elif type == 'health':
            return treasures['treasures'][value][self.__treasure_type][ran]['hp']
        elif type == 'spells':
            return Spell(treasures['treasures'][value][self.__treasure_type][ran]['name'], treasures['treasures'][value][self.__treasure_type][ran]['damage'],
                         treasures['treasures'][value][self.__treasure_type][ran]['mana_cost'], treasures['treasures'][value][self.__treasure_type][ran]['cast_range'])
        elif type == 'weapons':
            return Weapon(treasures['treasures'][value][self.__treasure_type][ran]['name'], treasures['treasures'][value][self.__treasure_type][ran]['damage'])
        else:
            raise Exception("Treasure type error")


t = Treasure()
