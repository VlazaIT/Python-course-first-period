1.
user = input('Enter your name: ')
print("Nice to meet you, " + user + "!")

2.
radius_str = input("Enter radius of circle: ")
radius = float(radius_str)
area = 3.14159 * radius * radius
print("Area of the circle =", area)

3.
length_str = input("Enter the length of the rectangle: ")
length = float(length_str)
width_str = input("Enter the width of the rectangle: ")
width = float(width_str)
perimeter = 2*(length+width)
area = length*width
print("Area of rectangle : ",area)
print("Perimeter of rectangle : ",perimeter)

4.
number1_str = input("Enter the first integer number: ")
number1 = float(number1_str)
number2_str = input("Enter the second integer number: ")
number2 = float(number2_str)
number3_str = input("Enter the third integer number: ")
number3 = float(number3_str)
Sum = number1 + number2 + number3
print("Sum of the numbers: ", Sum)
Product = number1 * number2 * number3
print("Multiplication of the numbers: ", Product)
Average = (number1 + number2 + number3)/3
print("Average of the numbers: ", Average)

5.
talents = input("Enter the weight in talents: \n")
pounds = input("Enter the weight in pounds: \n")
lots = input("Enter the weight in lots: \n")
kg = float(lots) * 13.3/1000 + float(pounds) * 13.3*32/1000 + float(talents) * 13.3*32*20/1000
grams = (kg - int(kg))*1000
print("The weight in modern units:")
print(int(kg), "kilograms and", round(grams, 2), "grams")

6.
import random
print("Random combinations of numbers for a 3-digit code combination lock (0-9): ")
for i in range(0, 3):
    y = random.randrange(10)
    print(y)
print("Random combinations of numbers for a 4-digit code combination lock (0-6): ")
for i in range(0, 4):
    y = random.randrange(7)
    print(y)