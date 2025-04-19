def double_numbers(numbers):
    # Loop through the list and double each element
    for i in range(len(numbers)):
        numbers[i] *= 2

def main():
    # Initial list of numbers
    numbers = [1, 2, 3, 4]
    
    # Print the original list
    print("Original list:", numbers)
    
    # Call the function to double each element
    double_numbers(numbers)
    
    # Print the modified list
    print("Doubled list:", numbers)

if __name__ == '__main__':
    main()
