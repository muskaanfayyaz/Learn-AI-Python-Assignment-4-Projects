def main():
    # Ask the user for a length in feet
    feet = float(input("Enter length in feet: "))

    # Convert feet to inches
    inches = feet * 12

    # Print the result
    print(f"{feet} foot{'s' if feet == 1 else 's'} is equal to {inches} inches.")

if __name__ == '__main__':
    main()
