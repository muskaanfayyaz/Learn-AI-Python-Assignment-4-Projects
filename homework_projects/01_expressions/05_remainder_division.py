def main():
    # Ask the user for the first integer
    dividend = int(input("Please enter an integer to be divided: "))
    
    # Ask the user for the second integer (divisor)
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Perform the division and calculate the remainder
    result = dividend // divisor
    remainder = dividend % divisor
    
    # Print the result and remainder
    print(f"The result of this division is {result} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
