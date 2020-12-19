import re

rules = {}
messages = []
# Used to work out where we are in the doc.
state = 0

# Add file lines to the relevant lists.
f = open("day19input.txt", "r")
for file_line in f:
    if file_line == '\n':
        state += 1
        continue
    if state == 0:
        rules[file_line.split(':')[0]] = file_line.rstrip().split(': ')[1]
    if state == 1:
        messages.append(file_line.rstrip())
f.close()


def create_regex(rule_no: str) -> str:
    if rules[rule_no] in ['"a"', '"b"']:
        return rules[rule_no].replace('"', '')
    rule_parts = rules[rule_no].split('|')

    out_parts = []
    for part in rule_parts:
        out_parts.append(''.join([create_regex(rule) for rule in part.split()]))

    return '(' + '|'.join(out_parts) + ')'


regex_for_0 = '^' + create_regex('0') + '$'

valid_messages = 0

for message in messages:
    if re.search(regex_for_0, message) is not None:
        valid_messages += 1
    # else:
    #     print(message + ' is valid')

print('No. valid messages: ' + str(valid_messages))
