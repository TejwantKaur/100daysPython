row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

pos = (input("Where you want to put your Treasure?\nEnter Row Column "))

row = int(pos[0])
col = int(pos[1])

map[row-1][col-1] = "🟦"
# sel_row = map[row-1]
# sel_row[col-1] = ""

# Outcome
print(f"{row1}\n{row2}\n{row3}")