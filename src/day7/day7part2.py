# Day 7 part 2
from day7.day7common import create_list_of_instructions


list_of_instructions = create_list_of_instructions()


# Returns the amount of bags in a bag.
def count_amount_in_bag(bag_colour: str) -> int:
    global list_of_instructions

    if list_of_instructions[bag_colour] == 0:
        return 0

    out = 0

    for colour in list_of_instructions[bag_colour].keys():
        # out = (count of bags in sub bag) + count of sub bag
        out += (list_of_instructions[bag_colour][colour] * count_amount_in_bag(colour)) + list_of_instructions[bag_colour][colour]

    return out


print('Amount of bags in shiny gold bag: ' + str(count_amount_in_bag('shiny gold')))
