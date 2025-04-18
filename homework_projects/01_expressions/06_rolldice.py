import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Print the results of each roll and the total
    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total of both dice: {die1 + die2}")

def main():
    print("Rolling two dice...")
    roll_dice()  # Call the function to simulate rolling the dice

if __name__ == '__main__':
    main()
