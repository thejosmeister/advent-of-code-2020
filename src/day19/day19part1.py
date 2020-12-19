"""
Day 19 Part 1

Pretty easy start making some verbose regex.
"""

import re
from day19.day19common import set_up, create_regex

[rules, messages] = set_up()

# Create regex for rule 0
regex_for_0 = '^' + create_regex('0', rules) + '$'

# We will check all the messages to see if they match the regex for rule 0.
valid_messages = list(filter(lambda message: (re.search(regex_for_0, message) is not None), messages))

print('No. valid messages: ' + str(len(valid_messages)))
