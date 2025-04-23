import random

def main():
    # Generate a random secret number between 1 and 99
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    # Prompt the user for their first guess
    guess = int(input("Enter a guess: "))

    # Continue looping until the guess matches the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Blank line for better formatting
        guess = int(input("Enter a new guess: "))

    # Congratulate the user on a correct guess
    print("Congrats! The number was: " + str(secret_number))


# This ensures the game only runs when the script is executed directly
if __name__ == '__main__':
    main()
