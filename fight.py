from enemy import Enemy
from hero import Hero
from termcolor import colored


class Fight:

    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy

    def start_fight(self):
        print(colored("A fight is started between", 'cyan', attrs=['bold']),
              colored(self.__hero.known_as(), 'green', attrs=['bold']), '(',
              colored("health", 'red', attrs=['bold']), '=', colored(
                  self.__hero.get_health(), 'red', attrs=['bold']),
              'and',
              colored('mana', 'blue', attrs=['bold']), '=', colored(
                  self.__hero.get_mana(), 'blue', attrs=['bold']),
              ')', 'and', colored('Enemy', 'red', attrs=['bold']),
              '(', colored("health", 'red', attrs=['bold']), '=', colored(
                  self.__enemy.get_health(), 'red', attrs=['bold']),
              'and',
              colored('mana', 'blue', attrs=['bold']), '=', colored(self.__enemy.get_mana(), 'blue', attrs=['bold']), ')')

        while True:
            self.__enemy.take_damage(
                self.__hero.attack(self.__hero.get_current_attack_method()))
            print(colored("Enemy", "red", attrs=['bold']), "health is",
                  colored(self.__enemy.get_health(), "red", attrs=['bold']))
            if(not self.__enemy.is_alive()):
                print(colored("Enemy", "red", attrs=['bold']), "is dead")
                print(colored(self.__hero.known_as(), "green", attrs=[
                      'blink', 'bold']), colored("WON!!!", 'cyan', attrs=['blink', 'bold']))
                break
            if not self.__enemy.location() == self.__enemy.location():
                self.__enemy.move_towards_hero()
            else:
                print(colored("Enemy", 'red', attrs=['bold']), "attacks for", colored(
                    self.__enemy.get_damage(), 'red', attrs=['bold']), "dmg")
                self.__hero.take_damage(self.__enemy.get_damage())
                print(colored(self.__hero.known_as(), "green", attrs=['bold']), "health is", colored(
                    self.__hero.get_health(), "red", attrs=['bold']))
                if(not self.__hero.is_alive()):
                    print(colored(self.__hero.known_as(), "green", attrs=['bold']), "is dead")
                    print(colored(self.__hero.known_as(), "red", attrs=[
                          'blink', 'bold']), colored("WON!!!", 'cyan', attrs=['blink', 'bold']))
                    break

    def __end_message(self):
        return "Fight ended"
