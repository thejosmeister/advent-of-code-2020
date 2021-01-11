"""
Day 23 Part 2

Using 'Vector memory' after looking for a hint as all my efforts fell short both by trying to spot a pattern and make
the process more memory efficient.

The vector_memory is a list where the entry at each index is the number of the cup to the right of the cup labelled
the index. This list starts with 0 to deal with there being no cup labelled 0.
"""

inp = '942387615'
list_size = 1000000

# This list is used to create the first part of our vector memory.
initial_list = [int(item) for item in list(inp)]
initial_list.append(10)

# Create the vector memory.
vector_memory = [0]
for i in range(1, list_size):
    if i < 10:
        vector_memory.append(initial_list[initial_list.index(i) + 1])
    else:
        vector_memory.append(i + 1)
vector_memory.append(initial_list[0])

# The current cup is at the start of our input.
current_cup = initial_list[0]


# This will find the next lowest cup left in the list after the current cup once we have removed the 3 cups.
def find_place_for_3(current_num: int, the_three: list) -> int:
    global list_size
    if (((current_num - 1) - 1) % list_size) + 1 in the_three:
        if (((current_num - 1) - 2) % list_size) + 1 in the_three:
            if (((current_num - 1) - 3) % list_size) + 1 in the_three:
                return (((current_num - 1) - 4) % list_size) + 1
            return (((current_num - 1) - 3) % list_size) + 1
        return (((current_num - 1) - 2) % list_size) + 1
    return (((current_num - 1) - 1) % list_size) + 1


# Get the cup next to the one specified.
def get_next_cup(cup: int) -> int:
    global vector_memory
    return vector_memory[cup]


# Play a round of the game.
def play_round():
    global list_size
    global vector_memory
    global current_cup

    # Get the 3 cups we are going to move.
    three_cups_start = get_next_cup(current_cup)
    three_cups_middle = get_next_cup(three_cups_start)
    three_cups_end = get_next_cup(three_cups_middle)

    # Find where to move the three cups and prepare for changes to the list.
    place_for_3 = find_place_for_3(current_cup, [three_cups_start, three_cups_middle, three_cups_end])
    after_three = get_next_cup(place_for_3)
    new_cup_after_current = get_next_cup(three_cups_end)

    # Make the changes required to the cup list.
    vector_memory[place_for_3] = three_cups_start
    vector_memory[three_cups_end] = after_three
    vector_memory[current_cup] = new_cup_after_current

    # Move to the next current cup
    current_cup = get_next_cup(current_cup)


# We will play 10000000 rounds.
for i in range(list_size * 10):
    if i % 100000 == 0:
        print('Round ' + str(i))

    play_round()


# Get the 2 numbers to the right of the 1 cup.
nums_next_to_1 = [get_next_cup(1), get_next_cup(get_next_cup(1))]

print('Numbers next to 1 multiplied together: ' + str(nums_next_to_1[0] * nums_next_to_1[1]))
