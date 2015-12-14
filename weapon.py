class Weapon:

    def __init__(self, name="The Axe of Destiny", damage=20):
        self._name = name
        self._damage = damage

    def __int__(self):
        return self._damage

    def __str__(self):
        return '{} - {}'.format(self._name, self._damage)

    def __repr__(self):
        return self.__str__()
