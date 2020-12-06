def decode(code, rows, cols):

    """
    Decode sent code and return its position.
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

    # Return position of sent.
    return rows[0], cols[0]

def get_sent_id(row, col):

    # Get position of sent and return its Sent ID.
    return row * 8 + col

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

highest_sent_id = ("", 0, 0, 0)

# Check each code in data list.
for code in data:

    # Clear the code.
    code = code.strip().replace("\n", "")

    # Get position of sent and its ID.
    row, col = decode(code, 128, 8)
    sent_id = get_sent_id(row, col)

    # Check if the Sent ID is higher than the previous ones.
    if sent_id > highest_sent_id[-1]:
        highest_sent_id = (code, row, col, sent_id)

# Show the result.
print("First Part: Code {} | Pos [{}, {}] | Sent ID {} ".format(*highest_sent_id))
