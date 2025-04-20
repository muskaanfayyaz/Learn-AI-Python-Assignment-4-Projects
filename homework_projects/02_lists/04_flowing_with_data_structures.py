# This function takes a list and some data,
# and adds the data to the list three times.
def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data) 

def main():
    # Ask user for a message
    message = input("Enter a message to copy: ")

    # Start with an empty list
    my_list = []

    # Show the list before modifying
    print("List before:", my_list)

    # Call the function (list will be modified inside)
    add_three_copies(my_list, message)

    # Show the list after modification
    print("List after:", my_list)

# Run the main function
if __name__ == "__main__":
    main()
