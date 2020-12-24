list_of_lines = []

f = open("test.txt", "r")
for file_line in f:
    list_of_lines.append(file_line.rstrip())
f.close()


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


black_tiles = []

for l in list_of_lines:
    flip = str(parse_to_coord(l))
    if flip in black_tiles:
        black_tiles.remove(flip)
    else:
        black_tiles.append(flip)

print(len(black_tiles))
print(black_tiles)
set_of_tiles_around = [[2, 0], [-2, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

count = 0
while count < 100:
    x_coords = []
    y_coords = []
    for b in black_tiles:
        x_coords.append(int(b.split('[')[1].split(',')[0]))
        y_coords.append(int(b.split(']')[0].split(', ')[1]))

    max_x = max(x_coords) + 2
    min_x = min(x_coords) - 2
    max_y = max(y_coords) + 1
    min_y = min(y_coords) - 1
    b_to_w = []
    w_to_b = []
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if x % 2 != y % 2:
                continue
            # print('x: ' + str(x) + ' y: ' + str(y))
            if str([x, y]) in black_tiles:
                count_of_black = 0
                for tile in set_of_tiles_around:
                    if str([x + tile[0], y + tile[1]]) in black_tiles:
                        count_of_black += 1

                if count_of_black == 0 or count_of_black > 2:
                    b_to_w.append(str([x, y]))
                continue

            # x,y in white
            count_of_black2 = 0
            for tile in set_of_tiles_around:
                if str([x + tile[0], y + tile[1]]) in black_tiles:
                    count_of_black2 += 1
            if count_of_black2 == 2:
                w_to_b.append(str([x, y]))

    # print(b_to_w)
    # print(w_to_b)
    for bt in b_to_w:
        black_tiles.remove(bt)
    for wt in w_to_b:
        black_tiles.append(wt)

    count += 1
    print('Day ' + str(count) + ': ' + str(len(black_tiles)))
    print('Max x' + str(max_x) + ', ' + str(min_x))
    print('Max y' + str(max_y) + ', ' + str(min_y))

