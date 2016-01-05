class Spell:

    def __init__(self, name='Fireball', damage=30, mana_cost=50, cast_range=2):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_mana_cost(self):
        return self._mana_cost

<<<<<<< HEAD
    def get_cast_rang(self):
        return self._cast_range
=======
    def get_cast_range(self):

        return self._cast_range

    def decrease_mana(self):
        mana = hero.get_mana()

>>>>>>> c3b262a56f6026d0dc8d44f3408074108d91c70b
