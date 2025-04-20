MAX_LENGTH = 3  # Only keep the first 3 elements

def shorten(lst):
    # Keep removing and printing the last element until the list is MAX_LENGTH long
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Removes the last element
        print("Removed:", removed)


def main():
    n = int(input("How many elements in the list? "))
    lst = []
    for i in range(n):
        element = input(f"Enter element #{i + 1}: ")
        lst.append(element)
    
    shorten(lst)
    print("Final list:", lst)

if __name__ == "__main__":
    main()
