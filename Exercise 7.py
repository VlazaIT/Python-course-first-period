#7.1

import calendar

season = ("spring", "summer", "autumn", "winter")
number_of_month = int(input("Please enter the number of a month (1-12): "))
print(calendar.month_name[number_of_month])

if number_of_month in (12,1,2):
    print(f"It is {season[3]} in that month.")
elif number_of_month in (3,4,5):
    print(f"It is {season[0]} in that month.")
elif number_of_month in (6,7,8):
    print(f"It is {season[1]} in that month.")
else:
    print(f"It is {season[2]} in that month.")

#7.2

names = set()
new_name = str(input("Enter the name: "))

while new_name != "":
    if new_name in names:
        print("Existing name")
    else:
        names.add(new_name)
        print("New name")
    new_name = str(input("Enter the name: "))

else:
    for n in names:
        print(n)
