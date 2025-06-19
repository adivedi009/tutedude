first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
    # Performing arithmetic operations
print(f'Addition: {first + second}')
print(f'Subtraction: {first - second}')
print(f'Multiplication: {first * second}')
try:
    print(f'Division: {first / second}')
except ZeroDivisionError:
    print("Division: Cannot divide by zero.")
