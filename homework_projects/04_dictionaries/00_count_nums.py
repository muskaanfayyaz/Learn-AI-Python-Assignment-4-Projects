def get_user_numbers():
    """
    Prompt the user to enter numbers until a blank line is entered.
    Returns a list of the entered numbers as integers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # Exit loop on blank input
        if user_input == "":
            break

        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list.
    Returns a dictionary with numbers as keys and their counts as values.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict

def print_counts(num_dict):
    """
    Print the number of times each number appears.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    """
    Main driver function.
    Gets numbers from the user, counts occurrences, and prints results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Standard Python entry point
if __name__ == '__main__':
    main()
