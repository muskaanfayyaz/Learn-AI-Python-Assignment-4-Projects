def get_first_element(lst):
    # Print the first element of the list
    print("First element:", lst[0])

def main():
    n = int(input("How many elements in the list? "))
    lst = []
    for i in range(n):
        element = input(f"Enter element #{i + 1}: ")
        lst.append(element)
    
    get_first_element(lst)

if __name__ == "__main__":
    main()
