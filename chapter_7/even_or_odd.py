number = input("Give me a number and I will tell you if it is even or odd. ")
number = int(number)

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")