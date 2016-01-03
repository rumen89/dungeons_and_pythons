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

        for f in self.matrix:
            print(f[:-1])

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

    def __find_hero_position(self):
        map = self.__read_file()

        for x in range(0, len(map)):
            for y in range(0, len(map[0])):
                if map[x][y] == 'S'or map[x][y] == 'H':
                    return (x, y)
        return False

    def spawn(self, hero):
        matrix = self.__read_file()

        hero_position = self.__find_hero_position()

        self.x = hero_position[0]
        self.y = hero_position[1]

        for i in range(hero_position[0], len(map)):
            for j in range(hero_position[1], len(map[0])):
                if map[i][j] == '.' or map[i][j] == 'T' or map[i][j] == 'S':
                    map[i][j] = 'H'
                    hero.set_x_position(i)
                    hero.set_y_position(j)
                    map[hero_position[0]][hero_position[1]]
                    print(map)
                    return True

        return False

    def move_hero(self, direction):
        if direction == "right":
            if self.len_column > self.x:
                if self.matrix[self.x][self.y + 1] == "#":
                    print("False")

                if self.matrix[self.x][self.y + 1] == ".":
                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y + 1], "H", 1)
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.y += 1
                    print("True")
                if self.matrix[self.x][self.y + 1] == "T":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y + 1], "H", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y], ".", 1)
                    self.x += 0
                    self.y += 1
                    print("Found treasure!")
            else:
                print("False")

        if direction == "down":
            if self.len_row > self.x:
                if self.matrix[self.x + 1][self.y] == "#":
                    print("False")

                if self.matrix[self.x + 1][self.y] == ".":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x + 1][self.y], "H", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.x += 1
                    self.y += 0
                    print("True")
                if self.matrix[self.x + 1][self.y] == "T":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x + 1][self.y], ".", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x+1][self.y], "H", 1)
                    print("Found treasure!")
                    self.x += 1
                    self.y += 0
            else:
                print("False")
        if direction == "left":
            if self.len_column > self.x and self.x >= 0:
                if self.matrix[self.x][self.y - 1] == "#":
                    print("False")

                if self.matrix[self.x][self.y - 1] == ".":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y - 1], "H", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y], ".", 1)
                    self.y -= 1
                    print("True")
                if self.matrix[self.x][self.y - 1] == "T":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y - 1], "H", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y], ".", 1)
                    self.y -= 1
                    print("Found treasure!")
            else:
                print("False")

        if direction == "down":
            if self.len_row > self.x:
                if self.matrix[self.x - 1][self.y] == "#":
                    print("False")

                if self.matrix[self.x - 1][self.y] == ".":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x + 1][self.y], "H", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.x -= 1
                    self.y += 0
                    print("True")
                if self.matrix[self.x - 1][self.y] == "T":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x - 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x + 1][self.y], ".", 1)
                    self.matrix[self.x - 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x+1][self.y], "H", 1)
                    print("Found treasure!")
                    self.x -= 1
            else:
                print("False")

        # print(self.matrix)

    def map_size(self):
        data = open(self.__file, 'r')
        self.matrix = data.readlines()
        self.len_row = len(self.matrix)
        self.len_column = len(self.matrix[0]) - 1
        data.close()

    def map_into_list(self):
        with open(self.__file, 'r') as f:
            string = f.read()
        string = string.split('\n')
        string = string[:-1]
        print()
