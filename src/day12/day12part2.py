"""
Day 12 part 2

Used 'w x' and 'w y' to denote waypoint positions.
Trickiest part was turning the waypoint correctly.
"""

navigation_instructions = []

f = open("day12input.txt", "r")
for file_line in f:
    navigation_instructions.append(file_line.rstrip())
f.close()


# Move waypoint relative to ship by specified distance and direction
def move_waypoint(_ship_pos: dict, direction: str, distance: int) -> dict:
    if direction == 'E':
        _ship_pos['w x'] += distance

    elif direction == 'W':
        _ship_pos['w x'] -= distance

    elif direction == 'N':
        _ship_pos['w y'] -= distance

    elif direction == 'S':
        _ship_pos['w y'] += distance

    return _ship_pos


# R90 x to y and y to -x
# 180 x to -x and y to -y
# L90 x to -y and y to x
def turn_waypoint(_ship_pos: dict, turn_instr: str) -> dict:
    if turn_instr in ['R90', 'L270']:
        new_x = -_ship_pos['w y']
        _ship_pos['w y'] = _ship_pos['w x']
        _ship_pos['w x'] = new_x

    elif turn_instr in ['L90', 'R270']:
        new_x = _ship_pos['w y']
        _ship_pos['w y'] = -_ship_pos['w x']
        _ship_pos['w x'] = new_x

    elif turn_instr in ['L180', 'R180']:
        _ship_pos['w x'] = -_ship_pos['w x']
        _ship_pos['w y'] = -_ship_pos['w y']

    return _ship_pos


# Move ship the relative distance to the way point a specified number of times
def move_ship_to_waypoint(_ship_pos: dict, times: int) -> dict:
    _ship_pos['x'] += _ship_pos['w x'] * times
    _ship_pos['y'] += _ship_pos['w y'] * times

    return _ship_pos


# Process each instruction and change ship or waypoint state appropriately
def process_instruction(_ship_pos: dict, instruction: str) -> dict:
    if instruction[0] in ['L', 'R']:
        _ship_pos = turn_waypoint(_ship_pos, instruction)

    elif instruction[0] in ['N', 'E', 'S', 'W']:
        _ship_pos = move_waypoint(_ship_pos, instruction[0], int(instruction[1:]))

    elif instruction[0] == 'F':
        _ship_pos = move_ship_to_waypoint(_ship_pos, int(instruction[1:]))

    return _ship_pos


# Initial ship and waypoint position
ship_pos = {'x': 0, 'y': 0, 'w x': 10, 'w y': -1}

# Process the list of instructions.
for nav_instruction in navigation_instructions:
    ship_pos = process_instruction(ship_pos, nav_instruction)

# Calculate Manhattan distance from [0,0]
dist_from_cen = abs(ship_pos['x']) + abs(ship_pos['y'])
print('Manhattan from centre: ' + str(dist_from_cen))
