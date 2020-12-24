

class CircularMemory:
    def __init__(self, input_list: list):
        self.mem = input_list

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

    def __init__(self, input_list: list):
        self.cups = CircularMemory(input_list)
        self.current_cup_value = self.cups.mem[0]
        self.list_of_currents = [self.cups.mem[0]]

    def output_from_cup_1(self) -> list:
        return self.cups.mem[self.cups.mem.index(1) + 1: self.cups.mem.index(1) + 10]

    def play_round(self):
        mod = len(self.cups.mem)
        the_3_cups = self.cups.remove_x_items_from_after_y(3, self.current_cup_value)

        if (((self.current_cup_value - 1) - 1) % mod) + 1 in the_3_cups:
            if (((self.current_cup_value - 1) - 2) % mod) + 1 in the_3_cups:
                if (((self.current_cup_value - 1) - 3) % mod) + 1 in the_3_cups:
                    self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 4) % mod) + 1)
                else:
                    self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 3) % mod) + 1)
            else:
                self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 2) % mod) + 1)
        else:
            self.cups.insert_list_after_x(the_3_cups, (((self.current_cup_value - 1) - 1) % mod) + 1)

        self.current_cup_value = self.cups.increment_pointer(self.current_cup_value)
        self.list_of_currents.append(self.current_cup_value)
        # print(self.cups.mem)
        # print(self.current_cup_value)


inp = ['942387615']
# inp = [ '978423615', '942387615']
big_lists = [[int(item) for item in list(inpu)] for inpu in inp]
list_size = 1000

for big_list in big_lists:
    for z in range(10, list_size + 1):
        big_list.append(z)

cup_lists = [CupList(big_list) for big_list in big_lists]

for i in range(list_size * 10):
    for cup_list in cup_lists:
        cup_list.play_round()


[print(cup_list.output_from_cup_1()) for cup_list in cup_lists]
# [print(cup_list.cups.mem) for cup_list in cup_lists]
# [print(cup_list.list_of_currents) for cup_list in cup_lists]

[print(x[list_size * 10 - x[::-1].index(1) + 1:list_size * 10 - x[::-1].index(1) + 10]) for x in [cup_list.list_of_currents for cup_list in cup_lists]]


# Values after one for list size
# 100 44,11
# 1000 568,45
# 10000 2750, 1762

# 24/12/20
# Looking at the values for the current cup it appears that the last time 1 is the current cup the next 2 current cups
# are the values right of 1 at the end. This appears to only work for #rounds = 10*len(input).
