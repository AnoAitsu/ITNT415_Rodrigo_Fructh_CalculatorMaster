def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def display_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose 1-5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print("Subtraction coming soon.")
        elif choice == "3":
            print("Multiplication coming soon.")
        elif choice == "4":
            print("Division coming soon.")


if __name__ == "__main__":
    main()