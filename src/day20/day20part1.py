"""
Day 20 Part 1

A quick and dirty go at part 1 just made a big dict of tiles and found the ones that had 2 sides not matching anything.
I worked on the assumption that each side was unique or had exactly one match and these were 'internal' matches.
"""

# Parsing input into dict of tiles.
line_of_tile = 0
tile_id = ''
tiles = {}
f = open("day20input.txt", "r")
for file_line in f:

    if 'Tile' in file_line:
        tile_id = file_line.rstrip().split(' ')[1].split(':')[0]
        tiles[tile_id] = {'tile': [], 'sides': {}}
        continue
    if file_line == '\n':
        continue
    tiles[tile_id]['tile'].append(file_line.rstrip())

f.close()


# Creates a dict of the left, right etc. sides.
def create_dict_of_sides(_tile: list) -> dict:
    return {'top': _tile[0], 'bottom': _tile[9][::-1], 'left': ''.join([_tile[i][0] for i in range(9, -1, -1)]),
            'right': ''.join([_tile[i][9] for i in range(0, 10)])}


for _id in tiles.keys():
    tiles[_id]['sides'] = create_dict_of_sides(tiles[_id]['tile'])


# See if two sides match regardless of orientation.
def match_side(main_side: str, other_side: str) -> bool:
    result = main_side == other_side or main_side == other_side[::-1]
    return result


# Want to see if our side will match any other sides for all the other tiles.
def check_if_side_matches_any_others(_side: str, id_containing_side: str) -> bool:
    for _id in tiles.keys():
        if _id == id_containing_side:
            continue
        for side_id in tiles[_id]['sides'].keys():
            if match_side(_side, tiles[_id]['sides'][side_id]):
                return True
    return False


# Identify the corner tiles.
corner_tiles = []
for _id in tiles.keys():
    num_of_outer = 0
    for side in tiles[_id]['sides'].keys():
        if not check_if_side_matches_any_others(tiles[_id]['sides'][side], _id):
            num_of_outer += 1

    if num_of_outer == 2:
        corner_tiles.append(_id)
    if num_of_outer > 2:
        print(_id + ' should not happen')

print('Corner tiles: ' + str(corner_tiles))

out = 1
for corner in corner_tiles:
    out *= int(corner)

print('Product of corner tiles: ' + str(out))
