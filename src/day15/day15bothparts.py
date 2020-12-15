"""
Day 15 both parts

This was quite a quick one, I had written the first part differently but this slightly more optimised soln works for
both parts. Part 2 is a bit slow but can get the answer in ~15 seconds.
"""


def day_15(ith_number: int) -> str:

    file_contents = []

    f = open("day15input.txt", "r")
    for file_line in f:
        file_contents.append(file_line.rstrip())
    f.close()

    # We will have a dict of the numbers with the 'index' of their last appearance
    list_of_nums = {}
    i = 1
    for string in file_contents[0].split(','):
        list_of_nums[string] = i
        i += 1

    # Can determine this from the fact there are no repeats in the start list.
    previous_number = '0'

    while i < ith_number:
        if previous_number in list_of_nums.keys():
            distance_to_previous = i - list_of_nums[previous_number]
            list_of_nums[previous_number] = i
            i += 1
            previous_number = str(distance_to_previous)
        else:
            list_of_nums[previous_number] = i
            i += 1
            previous_number = '0'

    return previous_number


print('Part 1: 2020th number is: ' + day_15(2020))
print('Part 2: 30000000th number is: ' + day_15(30000000))
