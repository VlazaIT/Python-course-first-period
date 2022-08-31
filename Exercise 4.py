4.1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1

4.2
inches = float(input("Enter an amount of inches: "))
while inches >= 0:
    cm = inches*2.54
    print(f"There is {cm} cm in {inches} inches")
    inches = float(input("Enter an amount of inches: "))
print("Program finished due to a negative value")

4.3
import sys
mylist = []
number = input("Enter a number: ")
if number == " ":
    print("Program finished, no max & min numbers")
    sys.exit()
mylist.append(number)
while number != " ":
    number = input("Enter a number: ")
    if number == " ":
        break
    mylist.append(number)
print(mylist)
print(f"The maximum number received from the user is {max(mylist)}")
print(f"The minimum number received from the user is {min(mylist)}")

4.4
import random
random_number = random.randint(1, 10)
guess_number = 0
while guess_number != random_number:
    guess_number = int(input("Enter the number between 1 and 10: "))
    if guess_number == random_number:
        print(f"Nice, you guessed it right: {guess_number}")
    elif guess_number > random_number:
        print("Oh, sorry, your guess is too high")
    else:
        print("Oh, sorry, your guess is too low")

4.5
import sys
correct_username = "python"
correct_password = "rules"
tries = 0
user_username = " "
user_password = " "
while (correct_username != user_username or correct_password != user_password):
    user_username = str(input("Enter your username: "))
    user_password = str(input("Enter your password: "))
    tries = tries + 1
    if tries == 5:
        print("Access denied")
        sys.exit()
    if (user_username != correct_username or user_password != correct_password):
        print("Please, enter the credentials again.")
print("You are welcome!")

4.6
import random
import math
n = 0
z = 0
N = int(input("Enter how many random points to generate: "))
while z <= N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = z +1
    if x*x+y*y < 1:
        n = n + 1
print(f"The approximate value of π is: {4*n/N}")
print(f"Real π= {math.pi}")