# Day 5 part 2
from day5.day5common import produce_list_of_seat_nos

# Sort the output
sorted_list = sorted(produce_list_of_seat_nos())

# Look for a difference larger than 1 for adjacent seat numbers.
for i in range(1, len(sorted_list)):
    if sorted_list[i] - sorted_list[i - 1] != 1:
        print(' ')
        print(sorted_list[i])
        print(sorted_list[i - 1])
