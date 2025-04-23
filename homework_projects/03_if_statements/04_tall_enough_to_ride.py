def tall_enough_extension():
    while True:
        user_input = input("How tall are you? ")

        # If the user enters nothing and presses Enter, stop the loop
        if user_input.strip() == "":
            print("Goodbye!")
            break

        # Try converting input to an integer
        try:
            height = int(user_input)
            if height >= 50:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number or press Enter to exit.")

# Run the function
tall_enough_extension()
