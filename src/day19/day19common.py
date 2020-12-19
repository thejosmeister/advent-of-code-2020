"""
Common stuff for day 19
"""


# Set up rules list and message list from input.
def set_up() -> list:
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

    return [rules, messages]


# Recursively creates a pretty chunky regex for each rule definition
def create_regex(rule_no: str, _rules: dict) -> str:
    if _rules[rule_no] in ['"a"', '"b"']:
        return _rules[rule_no].replace('"', '')

    # Just creating 1 liners to impress the ladies, makes me look smarter than I am (or more stupid...)
    return '(' + '|'.join([''.join([create_regex(rule, _rules) for rule in part.split()]) for part in _rules[rule_no].split('|')]) + ')'
