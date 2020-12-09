# Day 9 part 2


# Our invalid entry from part 1
invalid_num = 10884537

input_code = []

f = open("day9input.txt", "r")
for file_line in f:
    input_code.append(int(file_line.rstrip()))
f.close()

input_size = len(input_code)
set_of_nums = []


# Brute force through all the sums of contiguous numbers, put in a function so I can exit easily.
def funct():
    global input_code
    global invalid_num
    global input_size
    global set_of_nums
    for i in range(0, input_size):
        for j in range(i, input_size):

            total = sum(input_code[i:j])
            if total < invalid_num:
                continue
            if total > invalid_num:
                break

            # total = invalid_num
            set_of_nums = input_code[i:j]
            return 1
    return 0


# Run the above
funct()

if set_of_nums:
    print('Min in sum: ' + str(min(set_of_nums)))
    print('Max in sum: ' + str(max(set_of_nums)))
    print('Min + Max: ' + str(min(set_of_nums) + max(set_of_nums)))
