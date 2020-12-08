# Day 8 Part 1

from day8.GameConsole import GameConsole

input_code = []

f = open("day8input.txt", "r")
for file_line in f:
    input_code .append(file_line.rstrip())
f.close()


# Instantiate a game console
game_console = GameConsole(input_code)

game_console.run_without_repeat()

print('Accumulator value: ' + str(game_console.accumulator))
