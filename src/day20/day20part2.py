"""
Day 20 Part 2

This was the big daddy of all the days. Took me about half a day to write the thing only for it not to work. I spent the
rest of the day trying to find where the error was which was not made easy by my very untestable approach.

I left this for a day or 2 and then decided to run my input on someone else's soln to check if I was wildly out. I was
not and so I forced myself to take another look at where I could have gone wrong. It turned out I has used the wrong
side matching method in one of my methods (one is orientation agnostic) so once that was sorted I had the right answer.
Definitely would have benefited from some UTs!
"""
import math
import re
from day20.Tile import Tile

line_of_tile = 0
tile_id = ''
tiles = {}

# Create a dict of tiles
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


# The 'orientation agnostic' side match.
def match_side(main_side: str, other_side: str) -> bool:
    result = main_side == other_side or main_side == other_side[::-1]
    return result


# The pesky side match.
def strict_match_side(main_side: str, other_side: str) -> bool:
    return main_side == other_side


# Altered from pt1 to deal with the tile class.
def check_if_side_matches_any_others(_side: str, id_containing_side: str) -> bool:
    for _id in tiles.keys():
        if _id == id_containing_side:
            continue
        for side_id in tiles[_id].sides.keys():
            if match_side(_side, tiles[_id].sides[side_id]):
                return True
    return False


# Find all the corner, edge and then middle tiles.
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

# The methods below will find an appropriate corner, edge or middle tile to match the current tile. The 'new tile' will
# then be flipped and rotated so that the specified sides match.


# For an edge tile we specify where the outer side of the new tile must be facing (top, bottom etc.) and the side of
# the new tile which should match the existing side.
def find_edge_tile_to_match(tile_side: str, edge_side_must_be: str, match_on: str) -> Tile:
    global side_border_tiles

    # Find the tile with the matching side and remove from list of edge tiles.
    id_of_edge = ''
    for _id in side_border_tiles:
        for s in tiles[_id].sides.keys():
            if match_side(tile_side, tiles[_id].sides[s]):
                id_of_edge = _id

    side_border_tiles.remove(id_of_edge)
    next_tile = tiles[id_of_edge]

    # Orientate the tile to fit.
    while edge_side_must_be not in next_tile.edge_sides:
        next_tile.rotate_90_clockwise()

    # This is the match that was initially wrong and caused me all the pain.
    if not strict_match_side(tile_side, next_tile.sides[match_on]):
        if edge_side_must_be in ['left', 'right']:
            next_tile.reflect_horizontal()
        else:
            next_tile.reflect_vertical()

    # Error checking
    if not match_side(next_tile.sides[match_on], tile_side):
        print(match_on + ' not matching ' + tile_side + ' tile:')
        next_tile.to_string()

    return next_tile


# For a corner tile we specify where the outer sides of the new tile must be facing ([top, left], etc.) and the side of
# the new tile which should match the existing side.
def find_corner_tile_to_match(tile_side: str, edge_sides_must_be: list, side_to_match: str) -> Tile:
    global corner_tiles

    # Find the tile with the matching side and remove from list of corner tiles.
    id_of_edge = ''
    for _id in corner_tiles:
        for s in tiles[_id].sides.keys():
            if match_side(tile_side, tiles[_id].sides[s]):
                id_of_edge = _id

    corner_tiles.remove(id_of_edge)
    next_tile = tiles[id_of_edge]

    # Orientate the tile to fit.
    while not match_side(tile_side, next_tile.sides[side_to_match]):
        next_tile.rotate_90_clockwise()

    if not all(elem in edge_sides_must_be for elem in next_tile.edge_sides):
        if side_to_match in ['left', 'right']:
            next_tile.reflect_horizontal()
        else:
            next_tile.reflect_vertical()

    # Error checking
    if not strict_match_side(next_tile.sides[side_to_match], tile_side):
        print(side_to_match + ' not matching ' + tile_side + ' tile:')
        next_tile.to_string()

    return next_tile


# For a middle tile we specify we want to match on the top and left side of the new tile so we find the tile that
# matches on both and then orientate.
def find_internal_tile_to_match(left_tile_side: str, top_tile_side: str) -> Tile:
    global middle_tiles

    # Find the tile with the matching sides and remove from list of middle tiles.
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

    # Orientate the tile to fit.
    while not match_side(next_tile.sides['top'], top_tile_side):
        next_tile.rotate_90_clockwise()

    if not strict_match_side(next_tile.sides['top'], top_tile_side):
        next_tile.reflect_vertical()

    # Error checking
    if not strict_match_side(next_tile.sides['top'], top_tile_side):
        print('Top not matching ' + top_tile_side + ' tile:')
        next_tile.to_string()
    if not strict_match_side(next_tile.sides['left'], left_tile_side):
        print('left not matching ' + left_tile_side + ' tile:')
        next_tile.to_string()

    return next_tile


# We will build the image by starting with a corner and then rotating it so that it iis the top left tile. Then we find
# suitable tiles from left to right and make our way down the image.

# Make skeleton of image. This will be an array of the tiles where the tiles are in the right orientation.
image = []
dimension_of_image = int(math.sqrt(len(tiles.keys())))
[image.append([]) for i in range(dimension_of_image)]

# Sorting out the top corner tile.
top_corner = tiles[corner_tiles[0]]

while 'top' not in top_corner.edge_sides:
    top_corner.rotate_90_clockwise()
if 'left' not in top_corner.edge_sides:
    top_corner.reflect_vertical()

image[0].append(top_corner)
corner_tiles.remove(top_corner.id)

# Make up the top side.
for i in range(1, dimension_of_image - 1):
    image[0].append(find_edge_tile_to_match(image[0][i - 1].sides['right'], 'top', 'left'))

# Top right corner.
image[0].append(find_corner_tile_to_match(image[0][dimension_of_image - 2].sides['right'], ['top', 'right'], 'left'))

# Top line done so now do next 10 lines the same.
for i in range(1, dimension_of_image - 1):
    # Match edge tile.
    image[i].append(find_edge_tile_to_match(image[i - 1][0].sides['bottom'], 'left', 'top'))
    # Match middle tile.
    for j in range(1, dimension_of_image - 1):
        image[i].append(find_internal_tile_to_match(image[i][j - 1].sides['right'], image[i - 1][j].sides['bottom']))
    # Match edge tile.
    image[i].append(find_edge_tile_to_match(image[i][dimension_of_image - 2].sides['right'], 'right', 'left'))

# Do bottom row.
image[dimension_of_image - 1].append(
    find_corner_tile_to_match(image[dimension_of_image - 2][0].sides['bottom'], ['left', 'bottom'], 'top'))

for i in range(1, dimension_of_image - 1):
    image[dimension_of_image - 1].append(
        find_edge_tile_to_match(image[dimension_of_image - 1][i - 1].sides['right'], 'bottom', 'left'))

image[dimension_of_image - 1].append(
    find_corner_tile_to_match(image[dimension_of_image - 1][dimension_of_image - 2].sides['right'], ['right', 'bottom'],
                              'left'))

# Stitch the tiles together with borders still present.
picture_with_borders = []
line_of_picture = ''
for i in range(dimension_of_image):

    for j in range(10):
        line_of_picture = ''
        for k in range(dimension_of_image):
            line_of_picture += image[i][k].tile[j]
        picture_with_borders.append(line_of_picture)

# Remove the borders to make the final picture
picture = []
for i in range(10 * dimension_of_image):
    if i % 10 not in [0, 9]:
        picture.append(''.join(
            picture_with_borders[i][j] for j in list(filter(lambda x: (x % 10 not in [0, 9]), range(10 * dimension_of_image)))))

# Now we find the sea monsters
# Will do this by rotating the picture till we find matches on the lines of regex below.
print('\nFinding sea monsters\n')

sea_monster_regex_line_1 = '^.{18}(#|O).$'
sea_monster_regex_line_2 = '^(#|O).{4}(#|O){2}.{4}(#|O){2}.{4}(#|O){3}$'
sea_monster_regex_line_3 = '^.(#|O).{2}(#|O).{2}(#|O).{2}(#|O).{2}(#|O).{2}(#|O).{3}$'

number_of_sea_monsters = 0


# Finds the sea monsters and replaces #'s with O's where they are present.
def search_image_for_sea_monsters(_image: list) -> list:
    global number_of_sea_monsters
    for i in range(len(_image) - 2):
        for g in range(len(_image) - 19):
            if re.search(sea_monster_regex_line_1, _image[i][g:g + 20]) is not None:
                if (re.search(sea_monster_regex_line_2, _image[i + 1][g:g + 20]) is not None) and (
                        re.search(sea_monster_regex_line_3, _image[i + 2][g:g + 20]) is not None):
                    number_of_sea_monsters += 1
                    _image[i] = ''.join([_image[i][:g + 18], 'O', _image[i][g + 19:]])
                    _image[i + 1] = ''.join(
                        [_image[i + 1][:g], 'O', _image[i + 1][g + 1:g + 5], 'OO', _image[i + 1][g + 7:g + 11], 'OO',
                         _image[i + 1][g + 13:g + 17], 'OOO', _image[i + 1][g + 20:]])
                    _image[i + 2] = ''.join(
                        [_image[i + 2][:g + 1], 'O', _image[i + 2][g + 2:g + 4], 'O', _image[i + 2][g + 5:g + 7], 'O',
                         _image[i + 2][g + 8:g + 10], 'O', _image[i + 2][g + 11:g + 13], 'O',
                         _image[i + 2][g + 14:g + 16], 'O', _image[i + 2][g + 17:]])

    return _image


# Search picture and rotate if nothing found.
for i in range(4):
    picture = search_image_for_sea_monsters(picture)
    if number_of_sea_monsters > 0:
        [print(l) for l in picture]
        break

    # Turn picture 90 degrees
    picture = [''.join([picture[k][j] for k in range(len(picture) - 1, -1, -1)]) for j in range(len(picture))]

number_of_hash = 0

for line in picture:
    number_of_hash += line.count('#')

print('\nNumber of hashes left: ' + str(number_of_hash))
print('Number of sea monsters: ' + str(number_of_sea_monsters))
