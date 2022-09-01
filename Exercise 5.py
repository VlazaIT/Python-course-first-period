5.1

import random

dice_list = []
number_dice = int(input("How many dice to roll? "))

for n in range(number_dice):
    dice_value = random.randint(1,6)
    print(f"dice value: {dice_value}")
    dice_list.append(dice_value)

print(f"Sum of the numbers is {sum(dice_list)}")

5.2

fault = ""
number = 0
numbers = []

while number != fault:
    number = input("Enter number: ")
    if number == fault:
        break
    numbers.append(number)

modified_numbers = [float(i) for i in numbers]
print(modified_numbers)
modified_numbers.sort(reverse=True)
print(modified_numbers [0:5])

5.3

number = int(input("Enter an integer number: " ))

if number == 1:
    print("The number is not prime")
else:
    for i in range(2, number):
        if (number%i == 0):
            print("The number is not prime")
            break
    else:
        print("The number is prime")