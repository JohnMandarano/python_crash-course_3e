odd_numbers = []
# for value in range(1, 20, 2):
#     odd_numbers.append(value)
# for number in odd_numbers:
#     print(number)

# multiples_of_3 = []
# for value in range(3, 31, 3):
#     multiples_of_3.append(value)
# for number in multiples_of_3:
#     print(number)

# cubes = []
# for value in range(1,11):
#     cubes.append(value**3)
# for number in cubes:
#     print(number)

cubes_comp = [value**3 for value in range(1,11)]
for number in cubes_comp:
    print(number)