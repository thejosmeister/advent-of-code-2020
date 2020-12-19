
list_of_sums = []

# Create a list of lists to become an array of seats.
f = open("day18input.txt", "r")
for file_line in f:
    list_of_sums.append(file_line.rstrip().replace(" ",""))
f.close()


def find_trailing_bracket(calc: str) -> int:
    num_of_leading = 0
    for i in range(len(calc) - 1, -1, -1):
        if calc[i] == ")":
            num_of_leading += 1
        elif calc[i] == "(":
            if num_of_leading == 0:
                return i
            else:
                num_of_leading -= 1


def evaluate_calc(calc: str) -> int:
    if len(calc.replace("(", "")) == 1:
        return int(calc.replace("(", ""))
    # walk along term performing calculations
    if calc[-1].isnumeric():
        if calc[-2] == '+':
            return evaluate_calc(calc[:-2]) + int(calc[-1])
        if calc[-2] == '*':
            return evaluate_calc(calc[:-2]) * int(calc[-1])
    # If we get to bracket then call calc on bit inside
    index_of_bracket = find_trailing_bracket(calc[:-1])

    if index_of_bracket == 0:
        return evaluate_calc(calc[index_of_bracket + 1:-1])

    if calc[index_of_bracket - 1] == '+':
        return evaluate_calc(calc[:index_of_bracket - 1]) + evaluate_calc(calc[index_of_bracket + 1:-1])

    if calc[index_of_bracket - 1] == '*':
        return evaluate_calc(calc[:index_of_bracket - 1]) * evaluate_calc(calc[index_of_bracket + 1:-1])


def evaluate_line(line: str) -> int:
    return evaluate_calc(line)

list_of_answers = []

for _sum in list_of_sums:
    print(_sum)
    list_of_answers.append(evaluate_line(_sum))
    print(list_of_answers)

print(list_of_answers)
print(sum(list_of_answers))