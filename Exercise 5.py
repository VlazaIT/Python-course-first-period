5.1

import random

dice_list = []
number_dice = int(input("How many dice to roll? "))

for n in range(number_dice):
    dice_value = random.randint(1,6)
    print(f"dice value: {dice_value}")
    dice_list.append(dice_value)

print(f"Sum of the numbers is {sum(dice_list)}")

