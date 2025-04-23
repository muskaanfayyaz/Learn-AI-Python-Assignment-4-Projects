def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
                if amount_bought < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += price * amount_bought
                break
            except ValueError:
                print("Please enter a valid number.")
    
    print(f"\nYour total is ${total_cost:.2f}")


# No need to edit beyond this point
if __name__ == '__main__':
    main()
