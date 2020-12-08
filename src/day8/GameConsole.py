# Probably 2020's Intcode machine

class GameConsole:
    # Constructor takes the list of input commands.
    def __init__(self, _input: list):
        self.input = _input
        self.state = 0
        self.accumulator = 0
        self.states_entered = [0]

    # Process each instruction, will probably call out to other methods when it gets more complex
    def process_instruction(self, instruction: str):
        action = instruction[:3]

        if action == 'nop':
            self.state += 1
        elif action == 'acc':
            self.accumulator += int(instruction.split()[1])
            self.state += 1
        elif action == 'jmp':
            self.state += int(instruction.split()[1])

    # Normal non state checking run method
    def run(self):
        while self.state < len(self.input):
            self.process_instruction(self.input[self.state])

    # Checks if the machine has already been in the state and returns -1 if so.
    def run_without_repeat(self) -> int:
        while self.state < len(self.input):
            self.process_instruction(self.input[self.state])
            if self.state in self.states_entered:
                return -1
            else:
                self.states_entered.append(self.state)
        return 0
