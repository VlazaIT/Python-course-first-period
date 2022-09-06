#6.1

import random

def roll():
    value = random.randint(1,6)
    return value

value = 0
i = 0
while value != 6:
    value = roll()
    i = i + 1
    print(f"The result of the {i} round is {value}")

print(f"Since the result is 6, program is finished after {i} rounds")

#6.2

import random

def roll(max_value):
    value = random.randint(1,max_value)
    return value

value = 0
max_value = int(input("Enter the number of sides on the dice: "))
i = 0
while value != max_value:
    value = roll(max_value)
    i = i + 1
    print(f"The result of the {i} round is {value}")

print(f"Since the result is {max_value}, program is finished after {i} rounds")

