from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell
from fight import Fight

h = Hero()
e = Enemy()

h.equip(Weapon())
h.learn(Spell())

h.set_current_attack_method("spell")

f = Fight(h, e)
f.start_fight()
