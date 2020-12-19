import re

rules = {}
messages = []
# Used to work out where we are in the doc.
state = 0

# Add file lines to the relevant lists.
f = open("day19part2input.txt", "r")
for file_line in f:
    if file_line == '\n':
        state += 1
        continue
    if state == 0:
        rules[file_line.split(':')[0]] = file_line.rstrip().split(': ')[1]
    if state == 1:
        messages.append(file_line.rstrip())
f.close()

print('_messages length ' + str(len(messages)))


def create_regex(rule_no: str) -> str:
    if rules[rule_no] in ['"a"', '"b"']:
        return rules[rule_no].replace('"', '')

    rule_parts = rules[rule_no].split('|')

    out_parts = []
    for part in rule_parts:
        out_parts.append(''.join([create_regex(rule) for rule in part.split()]))

    return '(' + '|'.join(out_parts) + ')'


valid_superset = []

for d in range(1, 100):
    check = len(valid_superset)
    # ^(42)+(42){d}(31){d}$
    regex_to_end_them_all = '^' + create_regex('42') + '+' + create_regex('42') + '{' + str(d) + '}' + create_regex('31') + '{' + str(d) + '}$'

    # print(regex_to_end_them_all)

    valid_messages = []

    for message in messages:
        if re.search(regex_to_end_them_all, message) is not None:
            valid_messages.append(message)

    for m in valid_messages:
        if m not in valid_superset:
            valid_superset.append(m)
    if len(valid_superset) > check:
        print('there are now: ' + str(len(valid_superset)) + ' valid messages')

print('No. valid messages: ' + str(len(valid_superset)))
