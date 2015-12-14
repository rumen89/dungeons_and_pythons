class Character:

    def __init__(self, health=100, mana=100):
        self.__max_health = health
        self.__max_mana = mana
        self.__health = health
        self.__mana = mana

    def is_alive(self):
        return health > 0

    def can_cast(self):
        return __mana > 0

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def take_healing(self, healing_points):
        if not is_alive():
            return False
        else:
            if self.__health + healing_points > self.__max_health:
                self.__health == healing_points
            else:
                self.__health += healing_points
            return True

    def take_mana(self, mana_points):
        if mana_points > self.__max_mana:
            self.__mana = self.__max_mana
        else:
            self.__mana += mana_points

    def attack():
        pass

    def take_damage(self, damage):
        if damage > self.__health:
            self.health = 0
        else:
            self.health -= damage

    def equip(self, weapon):
        pass

    def learn(self, spell):
        pass
