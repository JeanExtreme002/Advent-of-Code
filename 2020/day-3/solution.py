def walk(data, width, height, step_x, step_y, search = "#"):

    coord_x, count = 0, 0

    for coord_y in range(0, height, step_y):

        if data[coord_y][coord_x] == search: count += 1
        coord_x += step_x

        if coord_x >= width: coord_x -= width

    return count

with open("input.txt") as file:
    data = list(map(lambda s: s.strip(), file.readlines()))

height = len(data)
width = len(data[0])

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
final_result = 1

for right, down in slopes:
    count = walk(data, width, height, right, down)
    final_result *= count
    print("Slope [{}, {}] = {} trees found!".format(right, down, count))

print("Final Result:", final_result)
