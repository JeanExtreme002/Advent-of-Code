def convert_to_bin(code):

    """
    Convert the seat code to binary.
    """

    binary_rule = {"B": 1, "F": 0, "R": 1, "L": 0}
    return [binary_rule[char] for char in code]

def is_my_seat(seat, y, x, seats):

    """
    Check whether the seat is the desired one.
    """

    try: return not seats[y][x] and seats[y - 1][x] and seats[y + 1][x] and seats[y][x - 1] and seats[y][x + 1]
    except IndexError: return False

def get_pos_of(bin_code, exp = None):

    """
    Calculate the position of the row or column.
    """

    # Get the highest index.
    if exp is None: exp = len(bin_code) - 1

    # If Back or Right -> Minimum position += 2 ** index (from highest to lowest).
    # Example (code = FBFBBFF):
    # Char (F) | Min. Position (0 + 0 = 0)   | min_pos += 0    (6)
    # Char (B) | Min. Position (0 + 32 = 0)  | min_pos += 2 ** (5)
    # Char (F) | Min. Position (32 + 0 = 32) | min_pos += 0    (4)
    # Char (B) | Min. Position (32 + 8 = 40) | min_pos += 2 ** (3)
    # Char (B) | Min. Position (40 + 4 = 44) | min_pos += 2 ** (2)
    # Char (F) | Min. Position (44 + 0 = 44) | min_pos += 0    (1)
    # Char (F) | Min. Position (44 + 0 = 44) | min_pos += 0    (0)
    # Result: Row (44)

    min_pos = (2 ** exp) if bin_code[::-1][exp] else 0
    return min_pos + (get_pos_of(bin_code, exp - 1) if exp else 0)

def get_seat_position(code):

    """
    Decode the seat code and return its position.
    """

    # Convert the code to binary.
    binary_code = convert_to_bin(code)

    # Get the position (row and column).
    row = get_pos_of(binary_code[:7])
    column = get_pos_of(binary_code[7:])

    # Return the values as integers.
    return int(row), int(column)

def get_seat_id(row, col):

    """
    Get position of the seat and return its Seat ID.
    """

    return row * 8 + col

def search_value_by(array, function):

    """
    Return a value from a two-dimensional array that is validated by a function.
    """

    # Check each row and column of the array.
    for row in range(len(array)):
        for column in range(len(array[row])):

            # If the result is True, the value found and its position will be returned.
            if function(array[row][column], row, column, array):
                return array[row][column], row, column

# Get data from file.
with open("input.txt") as file:
    data = [line.strip().replace("\n", "") for line in file.readlines()]

# Create a matrix of free seats.
seats = [[0 for c in range(8)] for r in range(128)]

# Seat with the highest ID (first part).
first_part_seat = ("", 0, 0, 0)

# Check each code in the list of codes.
for code in data:

    # Get the position of the seat and its ID.
    row, col = get_seat_position(code)
    seat_id = get_seat_id(row, col)

    # Check if the Seat ID is higher than the previous ones.
    if seat_id > first_part_seat[-1]:
        first_part_seat = (code, row, col, seat_id)

    # Occupy one of the positions in the list.
    seats[row][col] = 1

# Get the desired assent.
my_sent_pos = search_value_by(seats, is_my_seat)[1:]
second_part_seat = (*my_sent_pos, get_seat_id(*my_sent_pos))

# Show the results.
print("First Part: Code {} -> Pos [{}, {}] | Seat ID {} ".format(*first_part_seat))
print("Second Part: Code {} -> Pos [{}, {}] | Seat ID {}".format("x" * 10, *second_part_seat))
