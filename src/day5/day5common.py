# Common code for day 5

# Takes 'seat binary' and coverts to decimal.
# I may write my own bin to dec converter at some point but it's a Saturday morning so massive CBA.
def convert_seat_to_dec(seat: str) -> int:
    binary_version = ''
    for character in seat:
        if character == 'F' or character == 'L':
            binary_version += '0'
        else:
            binary_version += '1'

    return int(binary_version, 2)


# Computes seat number using method above
def compute_seat_no(binary_seat_no: str) -> int:
    row = convert_seat_to_dec(binary_seat_no[:7])
    column = convert_seat_to_dec(binary_seat_no[7:])

    return (row * 8) + column


# Returns a list of the converted seat numbers
def produce_list_of_seat_nos() -> list:
    list_of_binary_seat_nos = []
    actual_seat_nos = []

    f = open("day5input.txt", "r")
    for file_line in f:
        list_of_binary_seat_nos.append(file_line.rstrip())
    f.close()

    for seat_no in list_of_binary_seat_nos:
        actual_seat_nos.append(compute_seat_no(seat_no))

    return actual_seat_nos
