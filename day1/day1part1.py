# day1 part 1
# loop through list, try to find number = 2020 - num

input_list = []

f = open("day1input.txt", "r")

for line in f:
    input_list.append(int(line))

f.close()

for el1 in input_list:
    for el2 in input_list:
        if 2020 - el2 == el1:
            print("elt 1")
            print(el1)
            print("elt 2")
            print(el2)
            print(el1*el2)

