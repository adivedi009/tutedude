def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    first = get_integer("Enter the first number: ")
    second = get_integer("Enter the second number: ")
    # Performing arithmetic operations
    print(f'Addition: {first + second}')
    print(f'Subtraction: {first - second}')
    print(f'Multiplication: {first * second}')
    try:
        print(f'Division: {first / second}')
    except ZeroDivisionError:
        print("Division: Cannot divide by zero.")

if __name__ == "__main__":
    main()