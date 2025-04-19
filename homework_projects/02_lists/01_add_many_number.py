def add_many_numbers(numbers):
    """
    This function takes a list of numbers and returns their sum.
    
    :param numbers: List of numbers to be summed
    :return: Sum of the numbers in the list
    """
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    sum_of_numbers = add_many_numbers(numbers)
    print(f"The sum of {numbers} is {sum_of_numbers}")

if __name__ == "__main__":
    main()