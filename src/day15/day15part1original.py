"""
Day 15 Part 1 Original Soln

Pretty quick and dirty.
"""

file_contents = []

f = open("day15input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

list_of_nums = []

for string in file_contents[0].split(','):
    list_of_nums.append(int(string))
set_of_nums = list_of_nums.copy()
list_of_nums.append(0)


def find_previous_occurrence(number: int):
    distance_to_previous = list_of_nums[:-1][::-1].index(number) + 1
    list_of_nums.append(distance_to_previous)


while len(list_of_nums) < 2020:
    if list_of_nums[-1] in set_of_nums:
        find_previous_occurrence(list_of_nums[-1])
    else:
        set_of_nums.append(list_of_nums[-1])
        list_of_nums.append(0)

print(list_of_nums[-1])
