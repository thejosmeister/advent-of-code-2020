# Day 11 part 2
from day11.day11common import create_map_of_seats, is_space_occupied, main

map_of_seats = create_map_of_seats()

# Set up some constants
map_of_seats_height = len(map_of_seats)
map_of_seats_width = len(map_of_seats[0])


# False if there is not a seat in the square.
def is_seat(inp: str) -> bool:
    if inp == '.':
        return False
    return True


# Looks in the direction specified by the x and y increments for the first seat and returns whether it is occupied.
def is_seat_in_direction(_x, _y, x_increment: int, y_increment: int, _map_of_seats: list) -> int:
    _x_increment = x_increment
    _y_increment = y_increment
    while map_of_seats_height > _y + _y_increment > -1 and map_of_seats_width > _x + _x_increment > -1:
        if is_seat(_map_of_seats[_y + _y_increment][_x + _x_increment]):
            return is_space_occupied(_x + _x_increment, _y + _y_increment, _map_of_seats, map_of_seats_width, map_of_seats_height)
        _x_increment += x_increment
        _y_increment += y_increment
    return 0


# Uses the criteria to occupy or vacate a seat.
def occupy_seat(_x: int, _y: int, _map_of_seats: list) -> str:
    num_adj_occ = 0
    # fix x
    num_adj_occ += is_seat_in_direction(_x, _y, 0, 1, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, 0, -1, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, 1, 0, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, -1, 0, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, 1, 1, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, -1, 1, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, 1, -1, _map_of_seats)
    num_adj_occ += is_seat_in_direction(_x, _y, -1, -1, _map_of_seats)

    if num_adj_occ > 4:
        return 'L'
    elif num_adj_occ == 0:
        return '#'
    else:
        return _map_of_seats[_y][_x]


out = main(map_of_seats, occupy_seat, map_of_seats_width, map_of_seats_height)

print('Num of seats occupied: ' + str(out))
