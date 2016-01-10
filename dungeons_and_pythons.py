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
                self.__process_command(command)

    def __process_command(self, command):

        if command == "print":
            self.dungeon.print_map()
        else:
            if(self.__check_next(command) == "Move"):
                if command == "up":
                    if self.dungeon.move_hero("up"):
                        self.hero.set_y_position(
                            self.hero.get_y_position() - 1)
                elif command == "down":
                    if self.dungeon.move_hero("down"):
                        self.hero.set_y_position(
                            self.hero.get_y_position() + 1)
                elif command == "left":
                    if self.dungeon.move_hero("left"):
                        self.hero.set_x_position(
                            self.hero.get_x_position() - 1)
                elif command == "right":
                    if self.dungeon.move_hero("right"):
                        self.hero.set_x_position(
                            self.hero.get_x_position() + 1)
                else:
                    print("Wrong command")
            elif(self.__check_next(command) == "Exit"):
                print("Congratz")
                return
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
        print(x, y, position_symbol)
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
            return "Move"
        elif position_symbol == 'G':
            return "Exit"
        elif position_symbol == 'H':
            return "Move"
        else:
            return

if __name__ == '__main__':
    dp = DungeonsAndPythons()
    dp.main()
