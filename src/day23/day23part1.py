inp = '942387615'

class CircularMemory:
    def __init__(self, input_list: str):
        self.mem = [int(item) for item in list(input_list)]

    def item_at(self, point: int) -> int:
        modulus = len(self.mem)
        return self.mem[point % modulus]

    def remove_x_items_from_after_y(self, x: int, y: int) -> list:
        if x > len(self.mem):
            print('Cannot remove ' + str(x) + ' from memory')
        count = 0
        out = []
        index_of_y = self.mem.index(y)
        while count < x:
            if index_of_y + 1 >= len(self.mem):
                out.append(self.mem.pop(0))
            else:
                out.append(self.mem.pop(index_of_y + 1))
            count += 1
        return out

    def insert_list_after_x(self, list_to_insert: list, after_value: int):
        index_of_value = self.mem.index(after_value)
        if index_of_value == len(self.mem) - 1:
            self.mem = self.mem + list_to_insert
        else:
            self.mem = self.mem[:index_of_value + 1] + list_to_insert + self.mem[index_of_value + 1:]

    def increment_pointer(self, value: int) -> int:
        return self.mem[(self.mem.index(value) + 1) % len(self.mem)]


class CupList:

    def __init__(self, input_list: str):
        self.cups = CircularMemory(input_list)
        self.current_cup_value = self.cups.mem[0]

    def output_from_cup_1(self) -> str:
        return ''.join([''.join([str(item) for item in self.cups.mem[self.cups.mem.index(1) + 1:]]), ''.join([str(item) for item in self.cups.mem[:self.cups.mem.index(1)]])])

    def play_round(self):
        the_3_cups = self.cups.remove_x_items_from_after_y(3, self.current_cup_value)

        if (((self.current_cup_value - 1) - 1) % 9) + 1 in the_3_cups:
            if (((self.current_cup_value - 1) - 2) % 9) + 1 in the_3_cups:
                if (((self.current_cup_value - 1) - 3) % 9) + 1 in the_3_cups:
                    self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 4) % 9) + 1)
                else:
                    self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 3) % 9) + 1)
            else:
                self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 2) % 9) + 1)
        else:
            self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 1) % 9) + 1)

        self.current_cup_value = self.cups.increment_pointer(self.current_cup_value)

        print(self.cups.mem)
        print(self.current_cup_value)


cup_list = CupList(inp)

for i in range(100):
    cup_list.play_round()


print(cup_list.output_from_cup_1())

# 87592634 too high