# Day 9 part 1
# Quite a manual soln where we just loop through the previous 25 numbers seeing if they add up to the number in
# question.

input_code = []

f = open("day9input.txt", "r")
for file_line in f:
    input_code.append(int(file_line.rstrip()))
f.close()

input_size = len(input_code)


# Created a function so I could exit the process easily
def funct(index: int) -> int:
    global input_code
    # Finally remembered you have to set the increment to -1 for this to work.
    for j in range(index-1, index-26, -1):
        if input_code[j] == input_code[index]/2:
            continue
        else:
            for k in range(index-1, index-26, -1):
                if input_code[k] + input_code[j] == input_code[index]:
                    return 1

    return 0


# Main loop iterating through the input
for i in range(25, input_size):
    if funct(i) == 0:
        print('Invalid number: ' + str(input_code[i]))
        break
