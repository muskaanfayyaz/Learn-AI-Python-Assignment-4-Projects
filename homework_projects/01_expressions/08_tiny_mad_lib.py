def main():
    # Constants for sentence start
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
    
    # Prompt the user for inputs
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct the final sentence
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    
    # Print the fun sentence
    print(sentence)

if __name__ == '__main__':
    main()
