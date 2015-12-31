class Dungeon:
    def __init__(self, file):
        self.__file = file

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

    def print_map(self):
        with open(self.__file, 'r') as f:
            map = f.read()

        print(map)
        return map

    # def __find_free_psition(self, coordinates=(0, 0)):
    #     map = self.__read_file()

    #     for i in range(coordinates[0], len(map)):
    #         for j in range(coordinates[1], len(map[0])):
    #             if map[i][j] == 'S':
    #                 return (i, j)
    #             elif map[i][j] == '.' or map[i][j] == 'T':
    #                 return (i, j)

    #         return False

    def __find_hero_position(self):
        map = self.__read_file()

        for x in range(0, len(map)):
            for y in range(0, len(map[0])):
                if map[x][y] == 'S'or map[x][y] == 'H':
                    return (x, y)
        return False

    def spawn(self, hero):
        map = self.__read_file()

        hero_position = self.__find_hero_position

        for i in range(hero_position[0], len(map)):
            for j in range(hero_position[1], len(map[0])):
                if map[i][j] == '.' or map[i][j] == 'T' or map[i][j] == 'S':
                    map[i][j] = 'H'
                    hero.set_x_position(i)
                    hero.set_y_position(j)
                    mar[hero_position[0]][hero_position[1]]
                    return True

        return False

    def move_hero(self, direction):
        position = self.__find_hero_psition()

        if direction == 'up':
            if 
