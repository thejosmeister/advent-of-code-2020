# Day 11 part 1
from day11.day11common import create_map_of_seats, is_space_occupied, main

map_of_seats = create_map_of_seats()

# Set up some constants
map_of_seats_height = len(map_of_seats)
map_of_seats_width = len(map_of_seats[0])


# Uses the criteria to occupy or vacate a seat.
def occupy_seat(_x: int, _y: int, _map_of_seats: list) -> str:
    num_adj_occ = 0
    for i in range(-1,2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            num_adj_occ += is_space_occupied(_x + i, _y + j, _map_of_seats, map_of_seats_width, map_of_seats_height)

    if num_adj_occ > 3:
        return 'L'
    elif num_adj_occ == 0:
        return '#'
    else:
        return _map_of_seats[_y][_x]


out = main(map_of_seats, occupy_seat, map_of_seats_width, map_of_seats_height)

print('Num of seats occupied: ' + str(out))
