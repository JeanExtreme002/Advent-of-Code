def cmd_acc(current_instruction, value, accumulator):

    # Increase or decrease the accumulator.
    return current_instruction + 1, accumulator + value

def cmd_jmp(current_instruction, value, accumulator = 0):

    # Jump to a new instruction.
    return current_instruction + value, accumulator

def cmd_nop(current_instruction, value = 0, accumulator = 0):

    # Do nothing.
    return current_instruction + 1, accumulator

def execute(instruction, script, accumulator = 0):

    # Dictionary with functions for each command.
    instructions = {"acc": cmd_acc, "jmp": cmd_jmp, "nop": cmd_nop}

    # Separate the command and the value.
    command, value = script[instruction].strip().split()
    return instructions[command](instruction, int(value), accumulator)

# Get data from file.
with open("input.txt") as file:
    data = list(map(lambda s: s.replace("\n", ""), file.readlines()))

accumulator, current_instruction, log = 0, 0, []

# Run while there are still instructions.
while current_instruction != len(data):

    # Add instruction index to the log.
    log.append(current_instruction)

    # Executes the instruction and get the next instruction and a new value for accumulator.
    new_instruction, accumulator = execute(current_instruction, data, accumulator)

    # Checks whether the new instruction has already been executed.
    if new_instruction in log: break

    # Change the current instruction.
    current_instruction = new_instruction

# Show the result.
print("First Part: Accumulator - {} | Line - {}".format(accumulator, current_instruction + 1))
