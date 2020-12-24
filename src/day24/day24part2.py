"""
Day 24 part 2

Tried to look through an area initially but decided it wa faster to look around each black tile.
"""
from day24.day24common import create_initial_black_tiles

black_tiles = create_initial_black_tiles()

# So we can 'circle' a tile
set_of_tiles_around_tile = [[2, 0], [-2, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

count = 0
while count < 100:
    b_to_w = []
    w_to_b = []
    white_tiles_looked_at = []
    # Look around each black tile
    for black_tile in black_tiles:
        count_of_black = 0
        for tile in set_of_tiles_around_tile:
            x = black_tile[0] + tile[0]
            y = black_tile[1] + tile[1]
            if [x, y] in black_tiles:
                count_of_black += 1
            else:
                # If white then check if we have looked at this one before
                if [x, y] in white_tiles_looked_at:
                    continue
                white_tiles_looked_at.append([x, y])
                count_of_black2 = 0
                for _tile in set_of_tiles_around_tile:
                    if [x + _tile[0], y + _tile[1]] in black_tiles:
                        count_of_black2 += 1
                # Apply condition for white to black
                if count_of_black2 == 2:
                    w_to_b.append([x, y])
        # Apply condition for black to white
        if count_of_black == 0 or count_of_black > 2:
            b_to_w.append(black_tile)

    for bt in b_to_w:
        black_tiles.remove(bt)
    for wt in w_to_b:
        black_tiles.append(wt)

    count += 1
    print('Day ' + str(count) + ': ' + str(len(black_tiles)))

