from itertools import combinations as get_combinations

# Get data from file.
with open("input.txt") as file:
    data = list(map(int, file.readlines()))

# Get all combinations.
first_part_combinations = get_combinations(data, 2)
second_part_combinations = get_combinations(data, 3)

# Look for the two numbers that add up to 2020.
for numbers in first_part_combinations:
    if sum(numbers) == 2020: print("First Part: {}".format(numbers[0] * numbers[1]))

# Look for the three numbers that add up to 2020.
for numbers in second_part_combinations:
    if sum(numbers) == 2020: print("Second Part: {}".format(numbers[0] * numbers[1] * numbers[2]))
