"""
Common stuff for day 24
"""


# Parse the input line into an x, y coordinate
def parse_to_coord(line: str) -> list:
    line_list = list(line)
    x = 0
    y = 0
    while len(line_list) > 0:
        first = line_list.pop(0)
        if first in ['e', 'w']:
            if first == 'e':
                x += 2
                continue
            x -= 2
            continue
        second = line_list.pop(0)
        if first == 'n':
            if second == 'e':
                x += 1
                y -= 1
                continue
            x -= 1
            y -= 1
            continue
        # first == s
        if second == 'e':
            x += 1
            y += 1
            continue
        x -= 1
        y += 1
        continue

    return [x, y]


# Flip tile for each coord
def create_initial_black_tiles() -> list:
    list_of_lines = []

    f = open("day24input.txt", "r")
    for file_line in f:
        list_of_lines.append(file_line.rstrip())
    f.close()

    black_tiles = []

    for l in list_of_lines:
        flip = str(parse_to_coord(l))
        if flip in black_tiles:
            black_tiles.remove(flip)
        else:
            black_tiles.append(flip)

    return black_tiles
