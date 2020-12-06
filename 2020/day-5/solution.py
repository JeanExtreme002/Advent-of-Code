def decode_seat_code(code, rows, cols):

    """
    Decode seat code and return its position.
    """

    # Get lists of rows and columns.
    rows = [r for r in range(rows)]
    cols = [c for c in range(cols)]

    # Each character tells which half of a region the given seat is in.
    for char in code.upper():

        if char == "F": rows = rows[: round(len(rows) / 2)]    # Front (first : half)
        elif char == "B": rows = rows[round(len(rows) / 2) :]  # Back  (half  : last)
        elif char == "L": cols = cols[: round(len(cols) / 2)]  # Left  (first : half)
        elif char == "R": cols = cols[round(len(cols) / 2) :]  # Right (half  : last)

    # Return position of seat.
    return rows[0], cols[0]

def get_seat_id(row, col):

    # Get position of seat and return its Seat ID.
    return row * 8 + col

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

# Create a matrix of free seats.
seats = [[0 for i in range(8)] for r in range(128)]

# Seat with the highest ID (first part).
first_part_seat = ("", 0, 0, 0)

# Check each code in data list.
for code in data:

    # Clear the code.
    code = code.strip().replace("\n", "")

    # Get position of seat and its ID.
    row, col = decode_seat_code(code, len(seats), len(seats[0]))
    seat_id = get_seat_id(row, col)

    # Check if the Seat ID is higher than the previous ones.
    if seat_id > first_part_seat[-1]:
        first_part_seat = (code, row, col, seat_id)

    # Add seat to seats list.
    seats[row][col] = 1

# Check each row and column of the matrix.
for y in range(len(seats)):
    for x in range(len(seats[0])):

        # Check whether the seat is free and at the correct distance from other seats.
        try:
            if not seats[y][x] and seats[y - 1][x] and seats[y + 1][x] and seats[y][x - 1] and seats[y][x + 1]:
                second_part_seat = (y, x, get_seat_id(y, x))
                break

        # Even if an IndexError occurs, it will continue to search for the correct seat.
        except IndexError: continue

# Show the results.
print("First Part: Code {} | Pos [{}, {}] | Seat ID {} ".format(*first_part_seat))
print("Second Part: Code {} | Pos [{}, {}] | Seat ID {}".format("-" * 10, *second_part_seat))
