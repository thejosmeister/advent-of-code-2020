
from day8.GameConsole import GameConsole

input_code = []

f = open("day8input.txt", "r")
for file_line in f:
    input_code .append(file_line.rstrip())
f.close()


# Run it the first time to get the states entered
game_console = GameConsole(input_code)
game_console.run_without_repeat()

for state in game_console.states_entered:
    new_input_code = input_code.copy()
    # Change a jmp or nop
    if new_input_code[state][:3] == 'jmp':
        new_input_code[state] = 'nop'

    elif new_input_code[state][:3] == 'nop':
        new_input_code[state] = 'jmp' + new_input_code[state][3:]

    else:
        continue
    # Set up new console with the modified code
    new_game_console = GameConsole(new_input_code)

    if new_game_console.run_without_repeat() == 0:
        print('correct execution')
        print(new_game_console.accumulator)
        break

'''
smarter soln:

- look for jumps that exceed state, see if we can get to them (reverse execution?)
'''


