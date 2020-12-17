"""
Day 17 Part 2

Probably could have optimised the search area better as it too 5 mins + to run with an extra dimension.
"""
map_of_cores = []

# Create a list o
f = open("day17input.txt", "r")
for file_line in f:
    map_of_cores.append(list(file_line.rstrip()))
f.close()

max_x = len(map_of_cores[1])
max_y = len(map_of_cores)
max_z = 1
min_x = -1
min_y = -1
min_z = -1
max_w = 1
min_w = -1
active_cores = []

# Populate starting list of active cores.
for i in range(max_y):
    for j in range(max_x):
        if map_of_cores[i][j] == '#':
            active_cores.append([j, i, 0, 0])


# Works out if the core is now active as a result of the previous set of active cores.
def cell_is_now_active(coords: list, _active_cores: list) -> bool:
    num_adj_active = 0
    for x in range(coords[0] - 1, coords[0] + 2):
        for y in range(coords[1] - 1, coords[1] + 2):
            for z in range(coords[2] - 1, coords[2] + 2):
                for w in range(coords[3] - 1, coords[3] + 2):
                    if x == coords[0] and y == coords[1] and z == coords[2] and w == coords[3]:
                        continue
                    if [x, y, z, w] in _active_cores:
                        num_adj_active += 1

    if num_adj_active == 3:
        return True

    if coords in _active_cores and num_adj_active == 2:
        return True

    return False


# Activates/deactivates cores based on criteria. Dimensions of search area passed in.
def run_cycle(_dimensions: list, _active_cores: list) -> list:
    new_active_cores = []
    for x in range(_dimensions[0], _dimensions[1] + 1):
        for y in range(_dimensions[2], _dimensions[3] + 1):
            for z in range(_dimensions[4], _dimensions[5] + 1):
                for w in range(_dimensions[6], _dimensions[7] + 1):
                    if cell_is_now_active([x, y, z, w], _active_cores):
                        # This log message was useful for keeping track of the long run time.
                        print('Appending ' + str([x, y, z, w]))
                        new_active_cores.append([x, y, z, w])

    return new_active_cores


itr = 0
while itr < 6:
    # This log message was useful for keeping track of the long run time.
    print('Run cycle: ' + str(itr + 1))
    dimensions = [min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w]
    active_cores = run_cycle(dimensions, active_cores.copy())
    min_x -= 1
    min_y -= 1
    min_z -= 1
    min_w -= 1
    max_x += 1
    max_y += 1
    max_z += 1
    max_w += 1
    itr += 1

print('No. active cores: ' + str(len(active_cores)))
