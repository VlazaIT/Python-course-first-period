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

#6.3

def conversion(input):
    liters = input * 3.78541
    return liters

gallons = float(input("Enter gasoline volume in gallons: "))

while gallons >= 0:
    liters = conversion(gallons)
    print(f"There are {liters:.2f} liters in {gallons:.2f} gallons")
    gallons = float(input("Enter gasoline volume in gallons: "))
else:
    print("You entered a negative value")

#6.4

def summa(list):
    result = sum(list)
    return result

list = [1,3,10,5]
final_sum = summa(list)
print(f"The sum of the numbers is: {final_sum}")

#6.5

def removing(list_int):
    new_list = []
    for i in list_int:
        if i % 2 == 0:
            even = i
            new_list.append(even)
    return new_list

list_int = [0,1,2,3,4,5,6,7,8,9,10,11,-1,-2,-3,-4,-9,-1111110,-1]
print(f"Old list: {list_int}")
new_list = removing(list_int)
print(f"New list: {new_list}")

#6.6