3.1
zander_length = float(input("Write down the length of the zander in cm: "))
if zander_length < 42:
    print("Release the fish back into the lake since it is", 42 - zander_length, "cm below the size limit")
else:
    print("Zander's length is within the limit, you may keep the fish")

3.2
cabin_class = str(input("Enter your cabin class: "))
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window")
elif cabin_class == "B":
    print("Windowless cabin above the car deck")
elif cabin_class == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")

3.3
gender = str(input("Indicate your biological gender (Male/Female): "))
hemoglobin = float(input("Enter your hemoglobin level: "))
if gender == "Male":
    if hemoglobin < 134:
        print("You have a low hemoglobin value")
    elif hemoglobin > 167:
        print("You have a high hemoglobin value")
    else:
        print("Your hemoglobin level is normal")
elif gender == "Female":
    if hemoglobin < 117:
        print("You have a low hemoglobin value")
    elif hemoglobin > 155:
        print("You have a high hemoglobin value")
    else:
        print("Your hemoglobin level is normal")
else:
    print("Invalid biological gender entered")

3.4
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")