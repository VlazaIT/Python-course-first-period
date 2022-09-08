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

#7.3

airports = {"KLAX": "Los Angeles International Airport",
            "LFPG": "Charles de Gaulle Airport",
            "EHAM": "Amsterdam Airport Schiphol"}

choice = str(input("Would you like to enter a new airport (then type ENTER), fetch the information of an existing airport (then type FETCH) or quit (type QUIT): "))

while choice != "QUIT":
    if choice == "ENTER":
        new_airport_name = input("Enter new airport's name: ")
        new_airport_ICAO = input("Enter new airport's ICAO code: ")
        airports[new_airport_ICAO] = new_airport_name
    elif choice == "FETCH":
        existing_ICAO = input("Enter existing airport's ICAO code: ")
        if existing_ICAO in airports:
            print(f"{existing_ICAO} is ICAO code for {airports[existing_ICAO]}")
    choice = input("Would you like to enter a new airport (then type ENTER), fetch the information of an existing airport (then type FETCH) or quit (type QUIT): ")
# Used print to be sure all the airports were added to the dictionary
print(airports)