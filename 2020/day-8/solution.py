def cmd_acc(current_instruction, value, accumulator):

    # Increase or decrease the accumulator.
    return current_instruction + 1, accumulator + value

def cmd_jmp(current_instruction, value, accumulator = 0):

    # Jump to a new instruction.
    return current_instruction + value, accumulator

def cmd_nop(current_instruction, value = 0, accumulator = 0):

    # Do nothing.
    return current_instruction + 1, accumulator

def execute_instruction(instruction_index, script, accumulator = 0):

    """
    Execute an instruction and return a new instruction and a new accumulator.
    """

    # Dictionary with functions for each command.
    instructions = {"acc": cmd_acc, "jmp": cmd_jmp, "nop": cmd_nop}

    # Separate the command and the value.
    command, value = script[instruction_index].strip().split()
    return instructions[command](instruction_index, int(value), accumulator)

def get_all_indexes_of(value, iterable):

    """
    Return all indexes for a value.
    """

    # Convert the given object to a list.
    iterable = list(iterable)
    index_list = []

    # Get each index and store them in the list of indexes.
    for index in range(len(iterable)):
        if value in iterable[index]: index_list.append(index)

    # Return the list of indexes.
    return index_list

def replace_corrupted_instruction(script, instruction_index):

    """
    Return the copy of a script with the command (JMP or NOP) of a given instruction replaced.

    "jmp" -> "nop"
    "nop" -> "jmp"
    """

    # Copy the script and get the instruction by index.
    new_script = script.copy()
    instruction = script[instruction_index]

    # Replace the instruction.
    old, new = ("jmp", "nop") if "jmp" in instruction else ("nop", "jmp")
    new_script[instruction_index] = instruction.replace(old, new)

    # Return the new script.
    return new_script

def run(script):

    """
    Execute the program and return the accumulator, the last executed instruction
    and a boolean value, informing if the program finished without problems.
    """

    accumulator, current_instruction, log, corrupted = 0, 0, [], False

    # Run while there are still instructions.
    while current_instruction != len(script):

        # Add instruction index to the log.
        log.append(current_instruction)

        # Execute the instruction and get the next instruction and a new value for accumulator.
        new_instruction, accumulator = execute_instruction(current_instruction, script, accumulator)

        # Check whether the new instruction has already been executed.
        if new_instruction in log:
            corrupted = True
            break

        # Change the current instruction.
        current_instruction = new_instruction

    # Return the data.
    return accumulator, current_instruction + 1, not corrupted

# Get data from file.
with open("input.txt") as file:
    data = list(map(lambda s: s.replace("\n", ""), file.readlines()))

# Get the accumulator and the last instruction executed.
first_part_result = run(data)[: 2]

# Get indexes of "jmp" and "nop".
jmp_indexes = get_all_indexes_of("jmp", data)
nop_indexes = get_all_indexes_of("nop", data)
jmp_and_nop_indexes = jmp_indexes + nop_indexes

# Go through the list of indexes to find the corrupted command.
for index in jmp_and_nop_indexes:

    # Change the command and get a new script.
    new_script = replace_corrupted_instruction(data, index)

    # Execute the program.
    accumulator, last_instruction, finished = run(new_script)

    # Checks whether the new script works.
    if finished:
        second_part_result = (accumulator, last_instruction)
        break

# Show the result.
print("First Part: Accumulator - {} | Line - {}".format(*first_part_result))
print("Second Part: Accumulator - {} | Line - {}".format(*second_part_result))
