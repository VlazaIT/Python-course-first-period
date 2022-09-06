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