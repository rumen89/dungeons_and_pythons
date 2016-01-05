from character import Character
from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell
from treasure import Treasure
from fight import Fight
from dungeon import Dungeon


class DungeonsAndPythons:

    def __init__(self):
        self.hero = Hero()
        self.dungeon = Dungeon("level1.txt")
        self.hero.equip(Weapon())
        self.hero.learn(Spell())
        self.dungeon.spawn(self.hero)

    def main(self):
        print("Dungeons And Pythons")
        self.dungeon.print_map()
        self.__start_level()

    def __start_level(self):
        while True:
            command = input("Command>>")
            if command == "exit":
                break
            else:
                exit = self.__process_command(command)
                if exit == "exit":
                    break

    def __process_command(self, command):

        if command == "print":
            self.dungeon.print_map()
        else:
            if(self.__check_next(command) == "Move"):
                if command == "up":
                    if self.dungeon.move_hero("up"):
                        print('You went', command)
                        self.hero.set_y_position(
                            self.hero.get_y_position() - 1)
                    else:
                        print('You hit the wall')

                elif command == "down":
                    if self.dungeon.move_hero("down"):
                        print('You went', command)
                        self.hero.set_y_position(
                            self.hero.get_y_position() + 1)
                    else:
                        print('You hit the wall')
                elif command == "left":
                    if self.dungeon.move_hero("left"):
                        print('You went', command)
                        self.hero.set_x_position(
                            self.hero.get_x_position() - 1)
                    else:
                        print('You hit the wall')
                elif command == "right":
                    if self.dungeon.move_hero("right"):
                        print('You went', command)
                        self.hero.set_x_position(
                            self.hero.get_x_position() + 1)
                    else:
                        print('You hit the wall')
                else:
                    print("Wrong command")
            elif(self.__check_next(command) == "Exit"):
                print("Congratz")
                return "exit"
            else:
                pass

    def __check_next(self, command):
        x = self.hero.get_x_position()
        y = self.hero.get_y_position()

        if command == "up":
            y -= 1
        elif command == "down":
            y += 1
        elif command == "left":
            x -= 1
        elif command == "right":
            x += 1
        else:
            print("Error")
            return

        position_symbol = self.dungeon.get_position(x, y)
        if position_symbol is not None:
            return self.__commit_anction(position_symbol)
        else:
            return None

    def __commit_anction(self, position_symbol):
        if position_symbol == '.' or position_symbol == '#':
            return "Move"
        elif position_symbol == 'E':
            print("Enemy")
            enemy = Enemy()
            self.hero.set_current_attack_method("weapon")
            f = Fight(self.hero, enemy)
            f.start_fight()
            return "Move"

        elif position_symbol == 'T':
            self.__process_treasure()
            return "Move"
        elif position_symbol == 'G':
            return "Exit"
        elif position_symbol == 'H':
            return "Move"
        else:
            return

    def __process_treasure(self):
        treasure = Treasure()
        print('You fount a treasure type:', treasure.get_treasure_type())

        if treasure.get_treasure_type() == "weapons":
            print(treasure.loot_treasure())
            answer = input("Do you want to equip this weapon? y/n >>")
            if answer == 'y' or answer == 'yes':
                self.hero.equip(treasure.loot_treasure())
        elif treasure.get_treasure_type() == "spells":
            print(treasure.loot_treasure().get_name(), treasure.loot_treasure().get_damage(), 'dmg')
            answer = input("Do you want to learn this spell? y/n >>")
            if answer == 'y' or answer == 'yes':
                self.hero.learn(treasure.loot_treasure())
        elif treasure.get_treasure_type() == "mana":
            print(treasure.loot_treasure(), 'points')
            answer = input("Drink mana potion? y/n >>")
            if answer == 'y' or answer == 'yes':
                self.hero.take_mana(treasure.loot_treasure)
                print("Mana points: ", self.hero.get_mana())
        elif treasure.get_treasure_type() == "health":
            print(treasure.loot_treasure(), 'points')
            answer = input("Drink health potion? y/n >>")
            if answer == 'y' or answer == 'yes':
                self.hero.take_healing(treasure.loot_treasure())
                print("Health points: ", self.hero.get_health())

if __name__ == '__main__':
    dp = DungeonsAndPythons()
    dp.main()
