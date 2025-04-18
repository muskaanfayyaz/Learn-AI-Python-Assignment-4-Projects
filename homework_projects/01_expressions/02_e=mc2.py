# Constant for the speed of light in meters per second
SPEED_OF_LIGHT = 299_792_458  # m/s

def main():
    print("Einstein's Mass-Energy Equivalence Calculator")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter kilos of mass: ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            mass = float(user_input)
            energy = mass * SPEED_OF_LIGHT ** 2

            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s")
            print(f"{energy} joules of energy!\n")

        except ValueError:
            print("Invalid input. Please enter a number or type 'exit' to quit.\n")

if __name__ == '__main__':
    main()
