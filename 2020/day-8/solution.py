def acc(value, current_instruction, accumulator):

    # Increase or decrease the accumulator.
    return current_instruction + 1, accumulator + value

def jmp(value, current_instruction, accumulator):

    # Jump to a new instruction.
    return current_instruction + value, accumulator

def nop(value, current_instruction, accumulator):

    # Do nothing.
    return current_instruction + 1, accumulator

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

accumulator, current_instruction, log = 0, 0, []
instructions = {"acc": acc, "jmp": jmp, "nop": nop}

# Run while there are still instructions.
while current_instruction != len(data) and not current_instruction in log:

    # Separate the command and the value.
    command, value = data[current_instruction].strip().split()

    # Add instruction index to the log.
    log.append(current_instruction)

    # Executes the instruction and get the next instruction and a new value for accumulator.
    current_instruction, accumulator = instructions[command](int(value), current_instruction, accumulator)

# Show the results
print("First Part: Accumulator - {} | Command - \"{} {}\" | Line - {}".format(accumulator, command, value, current_instruction))
