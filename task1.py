list = []

for num in range(1000, 3001):
    if num % 9 == 0 and num % 5 != 0:
        list.append(str(num))

final_result = ','.join(list)
print(final_result)