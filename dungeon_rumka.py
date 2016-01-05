class Dungeon:
    def __init__(self, file):
        self.__file = file
        self.x = 0
        self.y = 0

    def __write_file(self, map_):
        with open(self.__file, 'w') as f:
            f.write(map_)

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

    def print_map(self):
        for f in self.matrix:
            print(f[:-1])

    def __find_hero_position(self):
        map = self.__read_file()

        for x in range(0, len(map)):
            for y in range(0, len(map[0])):
                if map[x][y] == 'S'or map[x][y] == 'H':
                    return (x, y)
        return False

    def spawn(self, hero):
        map = self.__read_file()

        hero_position = self.__find_hero_position()
        self.y = hero_position[1]
        self.x = hero_position[0]
        for i in range(hero_position[0], len(map)):
            for j in range(hero_position[1], len(map[0])):
                if map[i][j] == '.' or map[i][j] == 'T' or map[i][j] == 'S':
                    map[i][j] = 'H'
                    hero.set_x_position(i)
                    hero.set_y_position(j)
                    map[hero_position[0]][hero_position[1]]
                    return True
        return False

    def move_hero(self, direction):
        print('{}   {}'.format(self.x, self.y))
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
            elif self.matrix[self.x][self.y + 1] == "T":
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
                print("1False")

        elif direction == "down":
            if self.len_row > self.x:
                if self.matrix[self.x + 1][self.y] == "#":
                    print("False")

                elif self.matrix[self.x + 1][self.y] == ".":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x + 1][self.y], "H", 1)
                    self.matrix[self.x + 1] = self.matrix[self.x + 1]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.x += 1
                    self.y += 0
                    print("True")
                elif self.matrix[self.x + 1][self.y] == "T":
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
                print("2False")
        elif direction == "left":
            if self.len_column > self.x and self.x >= 0:
                if self.matrix[self.x][self.y - 1] == "#":
                    print("False")

                elif self.matrix[self.x][self.y - 1] == ".":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y - 1], "H", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y], ".", 1)
                    self.y -= 1
                    print("True")
                elif self.matrix[self.x][self.y - 1] == "T":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y - 1], "H", 1)

                    self.matrix[self.x] = self.matrix[self.x].replace(
                        self.matrix[self.x][self.y], ".", 1)
                    self.y -= 1
                    print("Found treasure!")
            else:
                print("3False")

        elif direction == "up":
            if self.len_row > self.x:
                if self.matrix[self.x - 1][self.y] == "#":
                    print("False")

                elif self.matrix[self.x - 1][self.y] == ".":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x - 1] = self.matrix[self.x - 1]\
                        .replace(self.matrix[self.x - 1][self.y], "H", 1)
                    self.matrix[self.x - 1] = self.matrix[self.x - 1]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.x -= 1
                    self.y += 0
                    print('{}   {}'.format(self.x, self.y))
                    print("True")
                elif self.matrix[self.x - 1][self.y] == "T":
                    self.matrix[self.x] = self.matrix[self.x]\
                        .replace(self.matrix[self.x][self.y], ".", 1)
                    self.matrix[self.x - 1] = self.matrix[self.x - 1]\
                        .replace(self.matrix[self.x - 1][self.y], ".", 1)
                    self.matrix[self.x - 1] = self.matrix[self.x - 1]\
                        .replace(self.matrix[self.x - 1][self.y], "H", 1)
                    print("Found treasure!")
                    self.x -= 1
            else:
                print("False")

        else:
            print('Wrong direction')

    # print(self.matrix)

    def map_size(self):
        data = open(self.__file, 'r')
        self.matrix = data.readlines()
        self.len_row = len(self.matrix)
        self.len_column = len(self.matrix[0]) - 1
        data.close()
