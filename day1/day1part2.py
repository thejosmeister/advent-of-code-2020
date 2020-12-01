# day1 part 2
# loop again

input_list = []

f = open("day1input.txt", "r")

for line in f:
    input_list.append(int(line))

f.close()

for el1 in input_list:
    for el2 in input_list:
        for el3 in input_list:
            if el1 + el2 + el3 == 2020:
                print(el1*el2*el3)

