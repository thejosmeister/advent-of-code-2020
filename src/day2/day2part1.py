# day 2 part 1


input_list = []

# I guess it would be less expensive to do all the calcs in here but cba.
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
    out['lower'] = int(limits[0])
    out['upper'] = int(limits[1])

    return out


# Recursive counter of character in string.
def recur_last_index(password: str, character: str) -> int:
    last_index = password.rfind(character)
    if last_index == -1:
        return 0
    else:
        return recur_last_index(password[:last_index], character) + 1


# Handles the recursive count.
def count_char(password: str, charachter: str) -> int:
    return recur_last_index(password, charachter)


# Evaluates whether each password and rule passes
def evaluate_rule(rule_and_passwd: dict) -> int:
    char_occurrences = count_char(rule_and_passwd['password'], rule_and_passwd['char'])
    if rule_and_passwd['lower'] <= char_occurrences <= rule_and_passwd['upper']:
        return 1
    else:
        return 0


num_of_good_passwords = 0

for elt in input_list:
    num_of_good_passwords += evaluate_rule(parse_rule_and_password(elt))

print(num_of_good_passwords)
