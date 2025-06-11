def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    number = get_integer("Enter the first number: ")
    print(f'The factorial of {number} is: {factorial(number)}')

if __name__ == "__main__":
    main()