"""
Day 19 Part 2

Took me a while to bother looking a bit more into the input to find you can create a set of 'super regexes' (regi?,
regecies?) that will cover all the rule permutations. I tested it up to d = 100000 but the number of valid messages
was the same as setting d = 5 so I am lucky I have the answer. I guess at some point the min allowable length for the
regex exceeds the longest message.
"""

import re
from day19.day19common import set_up, create_regex

[rules, messages] = set_up()


valid_superset = []
for d in range(1, 5):
    check = len(valid_superset)
    # ^(42)+(42){d}(31){d}$ is our super regex where 42 = 'regex for rule 42'
    regex_to_end_them_all = '^' + create_regex('42', rules) + '+' + create_regex('42', rules) + '{' + str(d) + '}' + \
                            create_regex('31', rules) + '{' + str(d) + '}$'

    valid_messages = list(filter(lambda message: (re.search(regex_to_end_them_all, message) is not None), messages))

    for m in valid_messages:
        if m not in valid_superset:
            # Make list of messages just the ones that haven't passed yet
            messages.remove(m)

            valid_superset.append(m)

    # Some logging for my sanity
    if len(valid_superset) > check:
        print('there are now: ' + str(len(valid_superset)) + ' valid messages and d = ' + str(d))

print('No. valid messages: ' + str(len(valid_superset)))
