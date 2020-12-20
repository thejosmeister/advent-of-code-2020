import math
import re
line_of_tile = 0
tile_id = ''
tiles = {}



class Tile:

    def __init__(self, id: str, tile: list, sides: dict, edge_sides: list, internal_sides: list):
        self.id = id
        self.tile = tile
        self.sides = sides
        self.edge_sides = edge_sides
        self.internal_sides = internal_sides

    def generate_sides(self):
        self.sides = {'top': self.tile[0], 'bottom': self.tile[9], 'left': ''.join([self.tile[i][0] for i in range(0, 10)]),
         'right': ''.join([self.tile[i][9] for i in range(0, 10)])}

    def rotate_edge_and_internal(self, side_name: str, right: bool) -> str:
        side_indexes = ['top', 'right', 'bottom', 'left']
        if right:
            return side_indexes[(side_indexes.index(side_name) + 1) % 4]
        return side_indexes[(side_indexes.index(side_name) - 1) % 4]

    def flip_edge_and_internal(self, side_name: str, vertical: bool) -> str:
        if vertical:
            side_indexes = ['right', 'left']
            if side_name in side_indexes:
                return side_indexes[(side_indexes.index(side_name) + 1) % 2]
            else:
                return side_name
        side_indexes = ['top', 'bottom']
        if side_name in side_indexes:
            return side_indexes[(side_indexes.index(side_name) + 1) % 2]
        else:
            return side_name

    def rotate_90_clockwise(self):
        new_tile = [''.join([self.tile[i][j] for i in range(9, -1, -1)]) for j in range(10)]
        self.tile = new_tile
        self.generate_sides()
        self.edge_sides = [ self.rotate_edge_and_internal(s, True) for s in self.edge_sides]
        self.internal_sides = [self.rotate_edge_and_internal(s, True) for s in self.internal_sides]


    def rotate_90_anticlock(self):
        new_tile = [''.join([self.tile[i][j] for i in range(10)]) for j in range(9, -1, -1)]
        self.tile = new_tile
        self.generate_sides()
        self.edge_sides = [self.rotate_edge_and_internal(s, False) for s in self.edge_sides]
        self.internal_sides = [self.rotate_edge_and_internal(s, False) for s in self.internal_sides]

    def rotate_180(self):
        self.rotate_90_clockwise()
        self.rotate_90_clockwise()

    def reflect_vertical(self):
        new_tile = [line[::-1] for line in self.tile]
        self.tile = new_tile
        self.generate_sides()
        self.edge_sides = [self.flip_edge_and_internal(s, True) for s in self.edge_sides]
        self.internal_sides = [self.flip_edge_and_internal(s, True) for s in self.internal_sides]

    def reflect_horizontal(self):
        self.tile.reverse()
        self.generate_sides()
        self.edge_sides = [self.flip_edge_and_internal(s, False) for s in self.edge_sides]
        self.internal_sides = [self.flip_edge_and_internal(s, False) for s in self.internal_sides]

    def to_string(self):
        print('id: ' + self.id)
        [print(line) for line in self.tile]
        print('Edge: ' + str(self.edge_sides))
        print('Internal: ' + str(self.internal_sides))


f = open("day20input.txt", "r")

for file_line in f:

    if 'Tile' in file_line:
        tile_id = file_line.rstrip().split(' ')[1].split(':')[0]
        tiles[tile_id] = Tile(tile_id, [], {}, [], [])
        continue
    if file_line == '\n':
        continue
    tiles[tile_id].tile.append(file_line.rstrip())

f.close()

[tiles[t].generate_sides() for t in tiles.keys()]


def match_side(main_side: str, other_side: str) -> bool:
    result = main_side == other_side or main_side == other_side[::-1]
    # print('main: ' + main_side + ' other: ' + other_side + ' result: ' + str(result))
    return result


def strict_match_side(main_side: str, other_side: str) -> bool:
    return main_side == other_side


def check_if_side_matches_any_others(_side: str, id_containing_side: str) -> bool:
    # print('checking if side: ' + _side + ' from ' + id_containing_side + ' tile matches any others')
    for _id in tiles.keys():
        if _id == id_containing_side:
            continue
        for side_id in tiles[_id].sides.keys():
            if match_side(_side, tiles[_id].sides[side_id]):
                # print('it does')
                return True
    # print('it doesnt')
    return False

# print(tiles)


corner_tiles = []
side_border_tiles = []
for _id in tiles.keys():
    num_of_outer = 0
    for side in tiles[_id].sides.keys():
        if not check_if_side_matches_any_others(tiles[_id].sides[side], _id):
            num_of_outer += 1
            tiles[_id].edge_sides.append(side)
        else:
            tiles[_id].internal_sides.append(side)

    if num_of_outer == 2:
        corner_tiles.append(_id)
    if num_of_outer == 1:
        side_border_tiles.append(_id)
    if num_of_outer > 2:
        print(_id + ' should not happen')

middle_tiles = list(filter(lambda x: (x not in corner_tiles and x not in side_border_tiles), tiles.keys()))
# print(len(middle_tiles))
# print(len(corner_tiles))
# print(len(side_border_tiles))
# print(len(tiles.keys()))

# Build image by starting with a corner
image = []
dimension_of_image = int(math.sqrt(len(tiles.keys())))
[image.append([]) for i in range(dimension_of_image)]
# want corner[0] to be image[0][0]
top_corner = tiles[corner_tiles[0]]

while 'top' not in top_corner.edge_sides:
    top_corner.rotate_90_clockwise()

if 'left' not in top_corner.edge_sides:
    top_corner.reflect_vertical()

print('\n\n\n')
top_corner.to_string()
print('\n\n\n')

image[0].append(top_corner)
corner_tiles.remove(top_corner.id)

def find_edge_tile_to_match(tile_side: str, edge_side_must_be: str, match_on: str) -> Tile:
    global side_border_tiles
    print('edge ' + str(side_border_tiles))
    id_of_edge = ''
    for _id in side_border_tiles:
        for s in tiles[_id].sides.keys():
            if match_side(tile_side, tiles[_id].sides[s]):
                id_of_edge = _id

    print('removing ' + id_of_edge)
    if id_of_edge == '':
        print(tile_side)
    side_border_tiles.remove(id_of_edge)
    next_tile = tiles[id_of_edge]

    while edge_side_must_be not in next_tile.edge_sides:
        next_tile.rotate_90_clockwise()

    if not match_side(tile_side, next_tile.sides[match_on]):
        if edge_side_must_be in ['left', 'right']:
            next_tile.reflect_horizontal()
        else:
            next_tile.reflect_vertical()

    if not match_side(next_tile.sides[match_on], tile_side):
        print(match_on + ' not matching ' + tile_side + ' tile:')
        next_tile.to_string()

    return next_tile


def find_corner_tile_to_match(tile_side: str, edge_sides_must_be: list, side_to_match: str) -> Tile:
    global corner_tiles
    print('corner ' + str(corner_tiles))
    id_of_edge = ''
    for _id in corner_tiles:
        for s in tiles[_id].sides.keys():
            if match_side(tile_side, tiles[_id].sides[s]):
                id_of_edge = _id

    corner_tiles.remove(id_of_edge)
    next_tile = tiles[id_of_edge]

    # all(elem in edge_sides_must_be for elem in next_tile.edge_sides)
    while not match_side(tile_side, next_tile.sides[side_to_match]):
        next_tile.rotate_90_clockwise()

    if not all(elem in edge_sides_must_be for elem in next_tile.edge_sides):
        if side_to_match in ['left', 'right']:
            next_tile.reflect_horizontal()
        else:
            next_tile.reflect_vertical()

    if not strict_match_side(next_tile.sides[side_to_match], tile_side):
        print(side_to_match + ' not matching ' + tile_side + ' tile:')
        next_tile.to_string()

    return next_tile


def find_internal_tile_to_match(left_tile_side: str, top_tile_side: str) -> Tile:
    global middle_tiles
    print('middle ' + str(middle_tiles))
    id_of_tile = ''
    for _id in middle_tiles:
        matches = 0
        for s in tiles[_id].sides.keys():
            if match_side(left_tile_side, tiles[_id].sides[s]):
                matches += 1
            if match_side(top_tile_side, tiles[_id].sides[s]):
                matches += 1
        if matches == 2:
            id_of_tile = _id

    middle_tiles.remove(id_of_tile)
    next_tile = tiles[id_of_tile]

    while not match_side(next_tile.sides['top'], top_tile_side):
        next_tile.rotate_90_clockwise()

    if not strict_match_side(next_tile.sides['top'], top_tile_side):
        next_tile.reflect_vertical()

    # check tile is right
    if not strict_match_side(next_tile.sides['top'], top_tile_side):
        print('Top not matching ' + top_tile_side + ' tile:')
        next_tile.to_string()
    if not strict_match_side(next_tile.sides['left'], left_tile_side):
        print('left not matching ' + left_tile_side + ' tile:')
        next_tile.to_string()

    return next_tile


for i in range(1, dimension_of_image - 1):

    image[0].append(find_edge_tile_to_match(image[0][i - 1].sides['right'], 'top', 'left'))
    print('found ' + str(0) + str(i) + ' tile id: ' + str(image[0][i].id))




# image[0][dimension_of_image - 2].to_string()
# for z in corner_tiles:
#     tiles[z].to_string()


image[0].append(find_corner_tile_to_match(image[0][dimension_of_image - 2].sides['right'], ['top', 'right'], 'left'))
print('found ' + str(0) + str(dimension_of_image - 1) + ' tile id: ' + str(image[0][dimension_of_image - 1].id))

# Top line done so now do next 10 lines the same
for i in range(1, dimension_of_image - 1):
    # match edge

    image[i].append(find_edge_tile_to_match(image[i - 1][0].sides['bottom'], 'left', 'top'))
    print('found ' + str(i) + str(0) + ' tile id: ' + str(image[i][0].id))
    # match middle
    for j in range(1, dimension_of_image - 1):

        image[i].append(find_internal_tile_to_match(image[i][j - 1].sides['right'], image[i - 1][j].sides['bottom']))
        print('found ' + str(i) + str(j) + ' tile id: ' + str(image[i][j].id))
    # match edge

    image[i].append(find_edge_tile_to_match(image[i][dimension_of_image - 2].sides['right'], 'right', 'left'))
    print('found ' + str(i) + str(dimension_of_image - 1) + ' tile id: ' + str(image[i][dimension_of_image - 1].id))

# Do bottom row

image[dimension_of_image - 1].append(find_corner_tile_to_match(image[dimension_of_image - 2][0].sides['bottom'], ['left', 'bottom'], 'top'))
print('found ' + str(dimension_of_image - 1) + str(0) + ' tile id: ' + str(image[dimension_of_image - 1][0].id))

for i in range(1, dimension_of_image - 1):

    image[dimension_of_image - 1].append(find_edge_tile_to_match(image[dimension_of_image - 1][i - 1].sides['right'], 'bottom', 'left'))
    print('found ' + str(dimension_of_image - 1) + str(i) + ' tile id: ' + str(image[dimension_of_image - 1][i].id))


image[dimension_of_image - 1].append(find_corner_tile_to_match(image[dimension_of_image - 1][dimension_of_image - 2].sides['right'], ['right', 'bottom'], 'left'))
print('found ' + str(dimension_of_image - 1) + str(dimension_of_image - 1) + ' tile id: ' + str(image[dimension_of_image - 1][dimension_of_image - 1].id))




for i in range(dimension_of_image):
    for j in range(dimension_of_image):
        print(str(i) + str(j) + ' ' + str(image[i][j].id))



picture = []
line_of_picture = ''
for i in range(dimension_of_image):

    for j in range(10):
        line_of_picture = ''
        for k in range(dimension_of_image):
            line_of_picture += image[i][k].tile[j]
        picture.append(line_of_picture)

[print(l) for l in picture]

newpic = []

for i in range(10 * dimension_of_image):
    if i % 10 not in [0, 9]:
        newpic.append(''.join(picture[i][j] for j in list(filter(lambda x: (x % 10 not in [0, 9]), range(10 * dimension_of_image)))))

[print(l) for l in newpic]

print('finding sea monsters')

sea_monster_regex_line_1 = '^.{18}(#|O).$'
sea_monster_regex_line_2 = '^[^\.].{4}(#|O){2}.{4}(#|O){2}.{4}(#|O){3}$'
sea_monster_regex_line_3 = '^.(#|O).{2}(#|O).{2}(#|O).{2}(#|O).{2}(#|O).{2}(#|O).{3}$'

number_of_sea_monsters = 0

def search_image_for_sea_monsters(_image: list) -> list:
    global number_of_sea_monsters
    for i in range(len(_image) - 1):
        # print('i = ' + str(i))
        for g in range(len(_image)):
            # print('j = ' + str(g))
            if re.search(sea_monster_regex_line_1, _image[i][g:g + 20]) is not None:
                # print('passed line 1 regex')
                if (re.search(sea_monster_regex_line_2, _image[i + 1][g:g + 20]) is not None) and (re.search(sea_monster_regex_line_3, _image[i + 2][g:g + 20]) is not None):
                    print('found sea monster: ' + str(i) + str(g))
                    number_of_sea_monsters += 1
                    _image[i] = ''.join([_image[i][:g + 18], 'O', _image[i][g + 19:]])
                    _image[i + 1] = ''.join([_image[i + 1][:g], 'O', _image[i + 1][g + 1:g + 5], 'OO', _image[i + 1][g + 7:g + 11], 'OO', _image[i + 1][g + 13:g + 17], 'OOO', _image[i + 1][g + 20:]])
                    _image[i + 2] = ''.join([_image[i + 2][:g+1], 'O', _image[i + 2][g + 2:g + 4], 'O', _image[i + 2][g + 5:g + 7], 'O', _image[i + 2][g + 8:g + 10], 'O', _image[i + 2][g + 11:g + 13], 'O', _image[i + 2][g + 14:g + 16], 'O', _image[i + 2][g + 17:]])

    return _image

the_image = newpic.copy()

number_of_hash = 0

for line in the_image:
    number_of_hash += line.count('#')

print('\n')
print('# hash before ' + str(number_of_hash))

for i in range(3):
    if i == 2:
        the_image = search_image_for_sea_monsters(the_image)

        # reflect vertically
        the_image = [line[::-1] for line in the_image]
        the_image = search_image_for_sea_monsters(the_image)

        # reflect back
        the_image = [line[::-1] for line in the_image]

        the_image.reverse()
        the_image = search_image_for_sea_monsters(the_image)
        the_image.reverse()
        [print(l) for l in the_image]
        print('\n')
        # [print(l) for l in the_image]
        print('\n')
    else:
        # turn 90 clock
        the_image = [''.join([the_image[k][j] for k in range(len(the_image) - 1, -1, -1)]) for j in range(len(the_image))]


number_of_hash = 0

for line in the_image:
    number_of_hash += line.count('#')

number_of_hash2 = 0

for line in newpic:
    number_of_hash2 += line.count('#')

print('\n')


print(number_of_hash)
print(number_of_hash2)
print(number_of_sea_monsters * 15)

newpic = [''.join([newpic[k][j] for k in range(len(newpic) - 1, -1, -1)]) for j in range(len(newpic))]
newpic = [''.join([newpic[k][j] for k in range(len(newpic) - 1, -1, -1)]) for j in range(len(newpic))]


[print(l) for l in newpic]
# 2176 too high




# comparison = []
# f = open("image.txt", "r")
# for file_line in f:
#     comparison.append(file_line.rstrip())
# f.close()
#
# number_of_hash2 = 0
#
# for line in comparison:
#     number_of_hash2 += line.count('#')
# print('\n')
#
# print(number_of_hash2)
#
# for i in range(24):
#     if comparison[i] != the_image[i]:
#         print(comparison[i])
#         print(the_image[i])
#         print(i)
#
# print('\n')
# [print(l) for l in comparison]
# print('\n')
