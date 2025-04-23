AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_input = input()  # Wait for user input
    while user_input != AFFIRMATION:
        print("Hmmm That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input()

    print("That's right! :)")

# Run the program
if __name__ == '__main__':
    main()
