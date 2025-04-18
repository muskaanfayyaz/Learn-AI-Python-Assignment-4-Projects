def main():
    anton: int = 21  # Anton's age is given as 21 years old
    beth: int = anton + 6  # Beth is 6 years older than Anton
    chen: int = beth + 20  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew is as old as Chen's age plus Anton's age
    ethan: int = chen  # Ethan is the same age as Chen

    # Print out all of the ages!
    print("Anton is " + str(anton) + " years old.")
    print("Beth is " + str(beth) + " years old.")
    print("Chen is " + str(chen) + " years old.")
    print("Drew is " + str(drew) + " years old.")
    print("Ethan is " + str(ethan) + " years old.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
