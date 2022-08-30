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


