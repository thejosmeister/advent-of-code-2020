"""
Day 17 Part 1

A bit of work to implement but worked 1st first time
"""
map_of_cores = []

# Create a list of lists to become an array of seats.
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
active_cores = []

# Populate starting list of active cores.
for i in range(max_y):
    for j in range(max_x):
        if map_of_cores[i][j] == '#':
            active_cores.append([j, i, 0])


# Works out if the core is now active as a result of the previous set of active cores.
def cell_is_now_active(coords: list, _active_cores: list) -> bool:
    num_adj_active = 0
    for x in range(coords[0] - 1, coords[0] + 2):
        for y in range(coords[1] - 1, coords[1] + 2):
            for z in range(coords[2] - 1, coords[2] + 2):
                if x == coords[0] and y == coords[1] and z == coords[2]:
                    continue
                if [x, y, z] in _active_cores:
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
                if cell_is_now_active([x, y, z], _active_cores):
                    new_active_cores.append([x, y, z])

    return new_active_cores


itr = 0
while itr < 6:
    dimensions = [min_x, max_x, min_y, max_y, min_z, max_z]
    active_cores = run_cycle(dimensions, active_cores.copy())
    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1
    itr += 1

print('No. active cores: ' + str(len(active_cores)))
