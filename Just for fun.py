import random
random_number = random.randint(1, 10)
print(random_number)
guess_number = int(input("Enter the number between 1 and 10: "))
if guess_number == random_number:
    print(f"Nice, you guessed it right: {guess_number}")
elif guess_number == random_number:
    print(f"Nice, you guessed it right: {guess_number}")
elif guess_number > random_number:
    print("Oh, sorry, your guess is too high")
elif guess_number < random_number:
    print("Oh, sorry, your guess is too low")

    while guess_number != random_number:
        guess_number = int(input("Enter the number between 1 and 10:"))
        if guess_number == random_number:
            print(f"Nice, you guessed it right: {guess_number}")
        elif guess_number > random_number:
            print("Oh, sorry, your guess is too high")
        else:
            print("Oh, sorry, your guess is too low")