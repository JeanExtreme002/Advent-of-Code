def decode(code, rows, cols):

    rows = [r for r in range(rows)]
    cols = [c for c in range(cols)]

    for char in code:

        if char == "F": rows = rows[0: round(len(rows) / 2)]
        elif char == "B": rows = rows[round(len(rows) / 2) :]
        elif char == "L": cols = cols[0: round(len(cols) / 2)]
        elif char == "R": cols = cols[round(len(cols) / 2) :]

    return rows[0], cols[0]

with open("input.txt") as file:
    data = file.readlines()

highest_sent_id = ("", 0, 0, 0)

for code in data:

    code = code.strip().replace("\n", "")
    row, col = decode(code, 128, 8)
    sent_id = row * 8 + col
    
    if sent_id > highest_sent_id[-1]:
        highest_sent_id = (code, row, col, sent_id)

print("First Part: Code {} | Pos [{}, {}] | Sent ID {} ".format(*highest_sent_id))
