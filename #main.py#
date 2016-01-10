from dungeon import Dungeon
from hero import Hero


def main():

    h = Hero()
    map = Dungeon('level1.txt')
    map.print_map()

    map.spawn(h)
    map.print_map()
    map.move_hero('right')
    map.print_map()
    h.take_damage(40)
    print(h.get_health())
    map.move_hero('down')
    print(h.get_health())
    map.print_map()
    map.move_hero('up')
    map.print_map()
    map.move_hero('left')
    map.print_map()
    map.move_hero('left')
    map.move_hero('up')
    map.move_hero('down')

#     map.map_size()
#     map.spawn(h)

# #    map.print_map()

#     map.move_hero('right')
#     map.print_map()
# #    map.move_hero('up')
#     map.move_hero('down')
#     map.print_map()
#     map.move_hero('up')
#     map.print_map()

if __name__ == '__main__':
    main()
