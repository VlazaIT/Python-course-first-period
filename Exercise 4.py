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