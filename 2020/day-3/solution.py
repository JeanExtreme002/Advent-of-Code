def get_count(array, value, step_x = 1, step_y = 1):

    """
    Return the number of times a value appears in a matrix.
    """

    x, count = 0, 0

    # Get size of the list.
    height , width = len(array), len(array[0])

    # Go through each row of the array.
    for y in range(0, height, step_y):

        # Check whether the value has been found.
        if data[y][x] == value: count += 1
        x += step_x

        # Check if the X is greater than the width. If so, the width
        # will be subtracted from the X to continue the walk.
        if x >= width: x -= width

    return count

# Get data from file.
with open("input.txt") as file:
    data = list(map(str.strip, file.readlines()))

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
final_result = 1

# Go through each slope to get the tree count.
for right, down in slopes:

    # Get the tree count and multiply the final result by it.
    count = get_count(data, "#", right, down)
    final_result *= count

    # Show the result of the current slope.
    print("Slope [{}, {}] = {} trees found.".format(right, down, count))

# Show the final result (second part).
print("Final Result:", final_result)
