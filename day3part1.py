map = []

# fill map

def increment_position( pos: list, map_width: int) -> list:
    pos[0] = (pos[0] + 3) % map_width
    pos[1] =+ 1
    return pos

def check_if_tree( pos: list, map: list ) -> int:
   if map[pos[1]][pos[0]] == '#':
        return 1
    else:
        return 0

width = len(map[0])
height = len(map)

Toboggan_position = [0,0]
total_trees = 0

while toboggan_position[0] < height - 2:
     toboggan_position = increment_position( toboggan_position,  width )
     total_trees =+ check_if_tree( toboggan_position, map )

print(total_trees)
