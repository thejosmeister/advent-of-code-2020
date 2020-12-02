# day 2 part 2


input_list = []

f = open("day2input.txt", "r")

for file_line in f:
    input_list.append(file_line)

f.close()

# input_list = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']


# Create a dict with all the relevant parts.
def parse_rule_and_password(line: str) -> dict:
    out = {}
    parts = line.split(': ')

    out['password'] = parts[1]

    out['char'] = parts[0][-1]

    limits = parts[0].split()[0].split('-')
    out['first'] = int(limits[0]) - 1
    out['second'] = int(limits[1]) - 1

    return out


# Gives the total times the char was in position, 0-2 times
def count_in_position(rule_and_passwd: dict) -> int:
    out = 0
    if rule_and_passwd['password'][rule_and_passwd['first']] == rule_and_passwd['char']:
        out += 1

    if rule_and_passwd['password'][rule_and_passwd['second']] == rule_and_passwd['char']:
        out += 1

    return out


# We only want the char to be in one of the positions.
def evaluate_rule(rule_and_passwd: dict) -> int:
    in_position = count_in_position(rule_and_passwd)

    if in_position == 1:
        return 1
    else:
        return 0


num_of_good_passwords = 0

for elt in input_list:
    num_of_good_passwords += evaluate_rule(parse_rule_and_password(elt))

print(num_of_good_passwords)
