# day 3 part 1

map_of_trees = []

# Fill map.
f = open("day3input.txt", "r")

for file_line in f:
    # The new lines were causing havoc initially as I forgot to rstrip them out
    map_of_trees.append(file_line.rstrip())

f.close()


# Increment toboggan position taking into account repeating map structure.
def increment_position(pos: list, map_width: int) -> list:
    pos[0] = (pos[0] + 3) % map_width
    pos[1] += 1
    return pos


# Checks if the square we are on is a tree (a #)
def check_if_tree(pos: list, tree_map: list) -> int:
    if tree_map[pos[1]][pos[0]] == '#':
        return 1
    else:
        return 0


width = len(map_of_trees[0])
height = len(map_of_trees)
toboggan_position = [0, 0]
total_trees = 0

while toboggan_position[1] < height - 1:
    toboggan_position = increment_position(toboggan_position, width)
    total_trees += check_if_tree(toboggan_position, map_of_trees)

print(str(total_trees) + ' trees in the path')
