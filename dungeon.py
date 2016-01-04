from random import randint


class Dungeon:

    def __init__(self, file):
        self.__file = file
        self.__level_map = self.__read_file()
        self.__x = 0
        self.__y = 0

    def __read_file(self):
        with open(self.__file, 'r') as f:
            m = f.read()

        map = []
        line = []

        for ch in m:
            if ch != '\n':
                line.append(ch)
            else:
                map.append(line)
                line = []
        return map

    def __write_file(self, map):
        with open(self.__file, 'w') as f:
            f.write(map)

    def __map_to_string(self):
        result = ''

        for line in self.__level_map:
            for ch in line:
                result += ch
            result += '\n'

        return result

    def print_map(self):
        print(self.__map_to_string())

    # def print_map(self):
    #     with open(self.__file, 'r') as f:
    #         map = f.read()

    #     print(map)
    #     return map

    # def __find_free_psition(self, coordinates=(0, 0)):
    #     map = self.__read_file()

    #     for i in range(coordinates[0], len(map)):
    #         for j in range(coordinates[1], len(map[0])):
    #             if map[i][j] == 'S':
    #                 return (i, j)
    #             elif map[i][j] == '.' or map[i][j] == 'T':
    #                 return (i, j)

    #         return False

    def find_hero_position(self):
        map = self.__read_file()

        for x in range(0, len(map)):
            for y in range(0, len(map[0])):
                if map[x][y] == 'S'or map[x][y] == 'H':
                    return (x, y)
        return False

    def spawn(self, hero):
        self.__hero = hero
        hero_position = self.find_hero_position()

        self.__x = hero_position[0]
        self.__y = hero_position[1]

        for i in range(hero_position[0], len(self.__level_map)):
            for j in range(hero_position[1], len(self.__level_map[0])):
                if self.__level_map[i][j] == '.' or self.__level_map[i][j] ==\
                   'T' or self.__level_map[i][j] == 'S':
                    self.__level_map[i][j] = 'H'
                    hero.set_x_position(i)
                    hero.set_y_position(j)
                    self.__x = i
                    self.__y = j
                    # print('{}   {}'.format(self.__x, self.__y))
                    self.__level_map[hero_position[0]][hero_position[1]]
                    return True

        return False

    def __get_map_size(self):
        return len(self.__level_map)

    def __get_line_size(self):
        return len(self.__level_map[0])

    def move_hero(self, direction):
        if direction == 'up':
            if self.__x - 1 < 0:
                return False
            elif self.__level_map[self.__x - 1][self.__y] == '#':
                return False
            elif self.__level_map[self.__x - 1][self.__y] == '.':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x - 1][self.__y] = 'H'
                self.__x -= 1
                return True
            elif self.__level_map[self.__x - 1][self.__y] == 'T':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x - 1][self.__y] = 'H'
                self.__x -= 1
                print('Found Treasure')
                return True
            elif self.__level_map[self.__x - 1][self.__y] == 'E':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x - 1][self.__y] = 'H'
                self.__x -= 1
                print('Enemyyyyy')
                return True
        elif direction == 'right':
            if self.__y + 1 >= self.__get_line_size():
                return False
            elif self.__level_map[self.__x][self.__y + 1] == '#':
                return False
            elif self.__level_map[self.__x][self.__y + 1] == '.':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x][self.__y + 1] = 'H'
                self.__y += 1
                return True
            elif self.__level_map[self.__x][self.__y + 1] == 'T':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x][self.__y + 1] = 'H'
                self.__y += 1
                print('Found Treasure')
                return True
            elif self.__level_map[self.__x][self.__y + 1] == 'E':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x][self.__y + 1] = 'H'
                self.__y += 1
                print('Enemyyyyyyy')
                return True
        elif direction == 'down':
            if self.__x + 1 >= self.__get_map_size():
                return False
            elif self.__level_map[self.__x + 1][self.__y] == '#':
                return False
            elif self.__level_map[self.__x + 1][self.__y] == '.':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x + 1][self.__y] = 'H'
                self.__x += 1
                return True
            elif self.__level_map[self.__x + 1][self.__y] == 'T':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x + 1][self.__y] = 'H'
                self.__x += 1
                print('Found Treasure')
                return True
                self.add_treasure(self.__pick_treasure())
            elif self.__level_map[self.__x - 1][self.__y] == 'E':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x - 1][self.__y] = 'H'
                self.__x -= 1
                print('Enemyyyy')
                return True
        elif direction == 'left':
            if self.__y - 1 < 0:
                return False
            elif self.__level_map[self.__x][self.__y - 1] == '#':
                return False
            elif self.__level_map[self.__x][self.__y - 1] == '.':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x][self.__y - 1] = 'H'
                self.__y -= 1
                return False
            elif self.__level_map[self.__x][self.__y - 1] == 'T':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x][self.__y - 1] = 'H'
                self.__y -= 1
                print('Found Treasure')
                return True
            elif self.__level_map[self.__x - 1][self.__y] == 'E':
                self.__level_map[self.__x][self.__y] = '.'
                self.__level_map[self.__x - 1][self.__y] = 'H'
                self.__x -= 1
                print('Enemyyyyyy')
                return True
        else:
            return False

    def __pick_treasure(self):
        list_treasure = ["mana", "health potion", "weapon", "spell"]

        index = randint(0, len(list_treasure) - 1)

        return list_treasure[index]

    def add_treasure(self, treasure):
        if treasure == 'health potion':
            # self.__hero.take_healing(100)
            print('Found health potion. Hero health is max.')
        elif treasure == 'mana':
            # self.__hero.take_mana(100)
            print('Found mana potion. Hero mana is max.')
        elif treasure == 'weapon':
            pass

    def get_position(self, x, y):
        try:
            return self.__level_map[y][x] if x > -1 and y > -1 else None
        except IndexError:
            return None
