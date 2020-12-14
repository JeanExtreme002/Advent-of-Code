def connect_adapters(adapters):

    """
    Connect all adapters and return the device's built-in joltage adapter rating and all differences found.
    """

    differences = [0, 0, 1]
    current_adapter = 0

    # Organize the list.
    adapters.sort()

    for index in range(len(adapters)):

        # Get the difference between the current adapter and the next adapter.
        difference = get_difference(current_adapter, adapters[index])
        if not difference: return

        differences[difference - 1] += 1
        current_adapter = adapters[index]

    return current_adapter + 3, differences

def get_difference(first_adapter, second_adapter):

    """
    If the connection between the adapters is valid, the joltage difference is returned.
    """

    difference = second_adapter - first_adapter
    return difference if difference in [1, 2, 3] else None

# Get data from file.
with open("input.txt") as file:
    data = [int(line) for line in file.readlines()]

# Get the device's built-in joltage adapter rating and all the differences found.
adapter, differences = connect_adapters(data)
first_part_result = differences[0] * differences[-1]

print("First Part:", first_part_result)
