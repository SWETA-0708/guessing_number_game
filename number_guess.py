import random

def no_guess():
    print("welcome to the number guessing game!")
    print("i have selected a random number between 1 and 100 .Try to guess it.")

    secret_number=random.randint(1,100)

    attempts=0
    while True:
        guess=int(input("enter your guess:"))
        attempts+=1

        if guess == secret_number:
            print(f"congratulations! you guessed the correct number in {attempts}")
            break
        elif guess < secret_number:
            print("too low!try again.")
        else:
            print("too high!try again.")

if __name__== "__main__":
    no_guess()