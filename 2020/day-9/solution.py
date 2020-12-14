from itertools import combinations as get_combinations

def get_contiguous_set(numbers, search, length = 2):

    """
    Return a contiguous set of at least two numbers in a list of
    numbers which sum to a given number.
    """

    for index in range(len(numbers) - length):

        # Get the contiguous set and organize it.
        contiguous_set = numbers[index: index + length]
        contiguous_set.sort()

        # Check the sum of the set.
        if sum(contiguous_set) == search: return contiguous_set

    # Try to find the number again, however, increasing the size of the set.
    return get_contiguous_set(numbers, search, length + 1)

def validate(numbers, index, range_):

    """
    Validate a value in the list of numbers using the XMAS cipher.
    """

    # Get all combinations of 2 numbers of the last X numbers before.
    combinations = get_combinations(numbers[index - range_ - 1: index], 2)

    # Check the sum of each combination.
    for combination in combinations:
        if sum(combination) == numbers[index]: return True

# Get data from file.
with open("input.txt") as file:
    data = [int(line) for line in file.readlines()]

preamble = 25

# Search for the invalid number.
for index in range(preamble + 1, len(data)):
    if not validate(data, index, preamble): break

# Get the contiguous set which sum to the invalid number.
contiguous_set = get_contiguous_set(data, data[index])

# Get the invalid number and the encryption weakness.
first_part_result = data[index]
second_part_result = sum([contiguous_set[0], contiguous_set[-1]])

# Show the results.
print("First Part: {} is the invalid number.".format(first_part_result))
print("Second Part: {} is the encryption weakness.".format(second_part_result))
