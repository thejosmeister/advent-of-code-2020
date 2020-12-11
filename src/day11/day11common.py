# Day 11 common stuff

def create_map_of_seats() -> list:
    map_of_seats = []

    # Create a list of lists to become an array of seats.
    f = open("day11input.txt", "r")
    for file_line in f:
        map_of_seats.append(list(file_line.rstrip()))
    f.close()

    return map_of_seats


# Checks if the space is present and occupied.
def is_space_occupied(_x: int, _y: int, _map_of_seats: list, width: int, height: int) -> int:
    if _x >= width or _x < 0:
        return 0
    if _y >= height or _y < 0:
        return 0
    if _map_of_seats[_y][_x] == '#':
        return 1
    return 0


# Compares the previous map of seats with the new one. Return True if they are the same.
def check_repeat(new: list, old: list, width: int, height: int) -> bool:
    for i in range(width):
        for j in range(height):
            if new[j][i] != old[j][i]:
                return False
    return True


# Main method that creates seat maps using the rules.
def main(map_of_seats: list, occupy_seat, map_of_seats_width: int, map_of_seats_height: int) -> int:
    while True:
        # Make new map of seats using occupation rules.
        y = 0
        new_map_of_seats = []
        for row_of_seats in map_of_seats:
            new_row_of_seats = []
            x = 0
            for seat in row_of_seats:
                if seat == '.':
                    new_row_of_seats.append('.')
                else:
                    new_row_of_seats.append(occupy_seat(x, y, map_of_seats))
                x += 1
            new_map_of_seats.append(new_row_of_seats)
            y += 1

        # Check if the new map is the same as the old.
        if check_repeat(new_map_of_seats, map_of_seats, map_of_seats_width, map_of_seats_height):
            break
        else:
            map_of_seats = new_map_of_seats

    # We reach here if the map of seats has repeated so now just count the occupied seats
    out = 0

    for i in range(map_of_seats_width):
        for j in range(map_of_seats_height):
            if map_of_seats[j][i] == '#':
                out += 1

    return out
