for intVal in range(1, 6):
    print(intVal)

even_nums = list(range(0, 10, 2))
for even_num in even_nums:
    print(even_num)

even_nums = list(range(1, 11))
squares = []
for even_num in even_nums:
    squares.append(even_num ** 2)
print(squares)

print(max(even_nums))
print(min(even_nums))
print(sum(even_nums))

squares2 = [value ** 2 for value in even_nums]
print(squares2)

print(squares2[-1])
