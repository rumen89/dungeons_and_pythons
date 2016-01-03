from dungeon import Dungeon
from hero import Hero


def main():

    h = Hero()
    map = Dungeon('level1.txt')
    map.map_size()
    map.spawn(h)

    map.print_map()

    map.move_hero('right')
    map.print_map()


if __name__ == '__main__':
    main()
