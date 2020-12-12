"""
Day 12 part 1

Fairly simple today, happy with my turn_ship() method.
"""
navigation_instructions = []

f = open("day12input.txt", "r")
for file_line in f:
    navigation_instructions.append(file_line.rstrip())
f.close()


# Move ship either N,E,S,W by a specified distance
def move_ship_in_direction(_ship_pos: dict, direction: str, distance: int ) -> dict:
    if direction == 'E':
        _ship_pos['x'] += distance

    elif direction == 'W':
        _ship_pos['x'] -= distance

    elif direction == 'N':
        _ship_pos['y'] -= distance

    elif direction == 'S':
        _ship_pos['y'] += distance

    return _ship_pos


# Work out the way the ship is facing
def turn_ship(_ship_pos: dict, direction: str, degrees: int) -> dict:
    face_list = ['N', 'E', 'S', 'W']
    new_face = 0
    current_face = face_list.index(_ship_pos['face'])
    if direction == 'R':
        new_face = (current_face + int(degrees/90)) % 4
    elif direction == 'L':
        new_face = (current_face - int(degrees / 90)) % 4

    _ship_pos['face'] = face_list[new_face]
    return _ship_pos


# Process each instruction and change ship state appropriately
def process_instruction(_ship_pos: dict, instruction: str) -> dict:
    if instruction[0] in ['L', 'R']:
        _ship_pos = turn_ship(_ship_pos, instruction[0], int(instruction[1:]))

    elif instruction[0] in ['N', 'E', 'S', 'W']:
        _ship_pos = move_ship_in_direction(_ship_pos, instruction[0], int(instruction[1:]))

    elif instruction[0] == 'F':
        _ship_pos = move_ship_in_direction(_ship_pos, _ship_pos['face'], int(instruction[1:]))

    return _ship_pos


# Initial ship position
ship_pos = {'x': 0, 'y': 0, 'face': 'E'}

# Process the list of instructions.
for nav_instruction in navigation_instructions:
    ship_pos = process_instruction(ship_pos, nav_instruction)

# Calculate Manhattan distance from [0,0]
dist_from_cen = abs(ship_pos['x']) + abs(ship_pos['y'])
print('Manhattan from centre: ' + str(dist_from_cen))
