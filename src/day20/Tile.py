"""

This class meant I had an easy way of rotating, flipping and accessing the properties of the tiles.

"""


class Tile:

    def __init__(self, id: str, tile: list, sides: dict, edge_sides: list, internal_sides: list):
        self.id = id
        self.tile = tile
        self.sides = sides
        self.edge_sides = edge_sides
        self.internal_sides = internal_sides

    # Each time we flip or rotate a tile we need to work out which side is which.
    def generate_sides(self):
        self.sides = {'top': self.tile[0], 'bottom': self.tile[9],
                      'left': ''.join([self.tile[i][0] for i in range(0, 10)]),
                      'right': ''.join([self.tile[i][9] for i in range(0, 10)])}

    # Used in the methods below.
    def rotate_edge_and_internal(self, side_name: str, right: bool) -> str:
        side_indexes = ['top', 'right', 'bottom', 'left']
        if right:
            return side_indexes[(side_indexes.index(side_name) + 1) % 4]
        return side_indexes[(side_indexes.index(side_name) - 1) % 4]

    # Used in the methods below.
    def flip_edge_and_internal(self, side_name: str, vertical: bool) -> str:
        if vertical:
            side_indexes = ['right', 'left']
            if side_name in side_indexes:
                return side_indexes[(side_indexes.index(side_name) + 1) % 2]
            else:
                return side_name
        side_indexes = ['top', 'bottom']
        if side_name in side_indexes:
            return side_indexes[(side_indexes.index(side_name) + 1) % 2]
        else:
            return side_name

    def rotate_90_clockwise(self):
        new_tile = [''.join([self.tile[i][j] for i in range(9, -1, -1)]) for j in range(10)]
        self.tile = new_tile
        self.generate_sides()
        self.edge_sides = [self.rotate_edge_and_internal(s, True) for s in self.edge_sides]
        self.internal_sides = [self.rotate_edge_and_internal(s, True) for s in self.internal_sides]

    def rotate_90_anticlock(self):
        new_tile = [''.join([self.tile[i][j] for i in range(10)]) for j in range(9, -1, -1)]
        self.tile = new_tile
        self.generate_sides()
        self.edge_sides = [self.rotate_edge_and_internal(s, False) for s in self.edge_sides]
        self.internal_sides = [self.rotate_edge_and_internal(s, False) for s in self.internal_sides]

    def rotate_180(self):
        self.rotate_90_clockwise()
        self.rotate_90_clockwise()

    def reflect_vertical(self):
        new_tile = [line[::-1] for line in self.tile]
        self.tile = new_tile
        self.generate_sides()
        self.edge_sides = [self.flip_edge_and_internal(s, True) for s in self.edge_sides]
        self.internal_sides = [self.flip_edge_and_internal(s, True) for s in self.internal_sides]

    def reflect_horizontal(self):
        self.tile.reverse()
        self.generate_sides()
        self.edge_sides = [self.flip_edge_and_internal(s, False) for s in self.edge_sides]
        self.internal_sides = [self.flip_edge_and_internal(s, False) for s in self.internal_sides]

    # A handy 'to string'.
    def to_string(self):
        print('id: ' + self.id)
        [print(line) for line in self.tile]
        print('Edge: ' + str(self.edge_sides))
        print('Internal: ' + str(self.internal_sides))
