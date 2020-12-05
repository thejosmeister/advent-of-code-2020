# day 3 part 2

map_of_trees = []

# Fill map.
f = open("day3input.txt", "r")

for file_line in f:
    map_of_trees.append(file_line.rstrip())

f.close()


# Increment toboggan position taking into account repeating map structure.
def increment_position(pos: list, map_width: int, increments: list) -> list:
    pos[0] = (pos[0] + increments[0]) % map_width
    pos[1] += increments[1]
    return pos


# Checks if the square we are on is a tree (a #)
def check_if_tree(pos: list, tree_map: list) -> int:
    if tree_map[pos[1]][pos[0]] == '#':
        return 1
    else:
        return 0


# Create a list of increments for the toboggan path.
# Used different while condition for the last increment [2, 1] , see below.
list_of_increments = [[1, 1], [3, 1], [5, 1], [7, 1]]
width = len(map_of_trees[0])
height = len(map_of_trees)
results = []

# Loop through 1st lot of increments.
for increment_pair in list_of_increments:
    toboggan_position = [0, 0]
    total_trees = 0
    while toboggan_position[1] < height - 1:
        toboggan_position = increment_position(toboggan_position, width, increment_pair)
        total_trees += check_if_tree(toboggan_position, map_of_trees)

    results.append(total_trees)


# Different y increment means a slightly different while condition (although it did work with the original condition as
# the height of the map is 323).
another_increment_pair = [1, 2]
toboggan_position = [0, 0]
total_trees = 0
while toboggan_position[1] < height - 2:
    toboggan_position = increment_position(toboggan_position, width, another_increment_pair)
    total_trees += check_if_tree(toboggan_position, map_of_trees)

results.append(total_trees)

print('Number of trees for each increment')
print(results)

final_amount = 1
for result in results:
    final_amount *= result

print('The totals multiplied together: ' + str(final_amount))
