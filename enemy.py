from character import Character


class Enemy(Character):

    def __init__(self, health=100, mana=100, damage=20):
        self.__damage = damage
        super(Enemy, self).__init__(health, mana)

    def get_damage(self):
        return self.__damage

    def moove_towards_hero(self, Hero):
        pass
