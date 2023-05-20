elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
even = []

# for number in elements:
#     print(number)

for index, number in enumerate(elements):
    if index % 2 == 0:
        even.append((index, number))
    else:
        odd.append((index, number))

print(f'Odd index: {odd}')
print(f'Even index: {even}')
