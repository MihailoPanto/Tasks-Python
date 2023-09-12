terminal_input = input("Enter sequence of whitespace separated words: ")

upper_num = 0
lower_num = 0

for char in terminal_input:
    if char.isupper():
        upper_num += 1
    elif char.islower():
        lower_num += 1

print(f"UPPER CASE {upper_num} LOWER CASE {lower_num}")