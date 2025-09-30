row1 = ["😂" , "🤣" , "😁"]
row2 = ["🤩" , "🥰" , "😘"]
row3 = ["😭" , "🥹" , "🥲"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

row = int(input ("which row do you want to input the treasure ?: "))
column = int(input ("which column do you want to input the treasure ?: "))


# call the desired row
selected_row = map[row - 1]
#[print(selected_row)

#edit one item from that desired row
selected_row[column -1] = "X"

print(f"{row1}\n{row2}\n{row3}")







