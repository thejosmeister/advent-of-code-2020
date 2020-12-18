
list_of_sums = []

# Create a list of lists to become an array of seats.
f = open("day18input.txt", "r")
for file_line in f:
    list_of_sums.append(list(file_line.rstrip()))
f.close()

def find_trailing_bracket(calc: str) -> int:


def evaluate_calc(calc: str) -> int:
    # walk along term performing calculations
    if calc[-1].isnumeric():
        if calc[-3] == '+':
            return evaluate_calc(calc[:-4]) + int(calc[-1])
        if calc[-3] == '*':
            return evaluate_calc(calc[:-4]) * int(calc[-1])
    # If we get to bracket then call calc on bit inside

def evaluate_brackets(calc: str) -> int:
    if '(' not in calc:
        return evaluate_calc(calc)

    return evaluate_brackets(calc[calc.find('(') + 1:find_trailing_bracket(calc)])

def evaluate_line(line: str) -> int:
    evaluate_calc(line)