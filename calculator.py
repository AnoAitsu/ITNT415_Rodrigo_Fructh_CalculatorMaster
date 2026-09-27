def add(a, b):
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b; raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero. Please enter a non-zero number.")
    return a / b


def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# ANSI color codes
RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"


def display_menu(selected_index=1):
    options = [
        ("+", "ADDITION"),
        ("-", "SUBTRACTION"),
        ("*", "MULTIPLICATION"),
        ("/", "DIVISION"),
        ("x", "EXIT"),
    ]
    width = 44

    print(CYAN + "╔" + "═" * width + "╗" + RESET)
    print(CYAN + "║" + RESET + BOLD + YELLOW + "CALCULATOR MASTER".center(width) + RESET + CYAN + "║" + RESET)
    print(CYAN + "╠" + "═" * width + "╣" + RESET)
    print(CYAN + "║" + " " * width + "║" + RESET)

    for i, (symbol, name) in enumerate(options, 1):
        pointer = ">" if i == selected_index else " "
        line = f"   {pointer} [{GREEN}{symbol}{RESET}] {name}"
        visible_len = len(f"   {pointer} [{symbol}] {name}")
        padding = " " * (width - visible_len)
        print(CYAN + "║" + RESET + line + padding + CYAN + "║" + RESET)

    print(CYAN + "║" + " " * width + "║" + RESET)
    print(CYAN + "╠" + "═" * width + "╣" + RESET)
    print(CYAN + "║" + RESET + "A: SELECT          B: BACK".center(width) + CYAN + "║" + RESET)
    print(CYAN + "╚" + "═" * width + "╝" + RESET)


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
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            try:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()