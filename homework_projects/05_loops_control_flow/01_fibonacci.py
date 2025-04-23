MAX_TERM_VALUE: int = 10000  # Maximum value for Fibonacci terms

def main():
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print on the same line with space
        # Generate the next term
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()
