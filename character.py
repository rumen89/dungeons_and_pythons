class Character:

    def __init__(self, health=100, mana=100):
        self.__max_health = health
        self.__max_mana = mana
        self.__health = health
        self.__mana = mana
        self.__spell = None
        self.__weapon = None
        self.__current_attack_method = "weapon"
        self.__x_position = 0
        self.__y_position = 0

    def set_x_position(self, x):
        self.__x_position = x

    def get_x_position(self):
        return self.__x_position

    def set_y_position(self, y):
        self.__y_position = y

    def get_y_position(self):
        return self.__y_position

    def is_alive(self):
        return self.__health > 0

    def can_cast(self):
        return self.__mana > 0

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def get_spell(self):
        return self.__spell

    def get_weapon(self):
        return self.__weapon

    def get_current_attack_method(self):
        return self.__current_attack_method

    def set_current_attack_method(self, method):
        self.__current_attack_method = method

    def lower_mana(self, mana_points):
        if self.__mana - mana_points <= 0:
            self.__mana = 0
        else:
            self.__mana -= mana_points

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

    def take_damage(self, damage):
        if damage > self.__health:
            self.__health = 0
        else:
            self.__health -= damage

    def equip(self, weapon):
        self.__weapon = weapon

    def learn(self, spell):
        self.__spell = spell

    def location(self):
        return [self.__x_position, self.__y_position]
