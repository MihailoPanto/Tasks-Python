terminal_input = input("Enter sequence of whitespace separated words: ")

list = terminal_input.split(" ")
final_list = []

for word in list:
    if word not in final_list:
        final_list.append(word)

final_list.sort()
print(' '.join(final_list))