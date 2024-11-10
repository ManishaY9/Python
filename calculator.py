def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# def divide(a, b):
#     return a / b if b != 0 else "Error: Division by zero"

# def modulus(a, b):
#     return a % b if b != 0 else "Error: Modulus by zero"
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Modulus by zero"
    
def power(a, b):
    return a ** b

def calculate(a, b, operation):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': modulus,
        '**': power
    }
    func = operations.get(operation)
    return func(a, b) if func else "Invalid operation"

# Example usage:
# print(calculate(10, 5, '+'))   # Output: 15
# print(calculate(10, 5, '-'))   # Output: 5
# print(calculate(10, 5, '*'))   # Output: 50
# print(calculate(10, 5, '/'))   # Output: 2.0
# print(calculate(10, 5, '%'))   # Output: 0
# print(calculate(10, 5, '**'))  # Output: 100000

# Interactive user input
# try:
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))
#     operation = input("Enter an operation (+, -, *, /, %, **): ")

#     result = calculate(a, b, operation)
#     print("Result:", result)
# except ValueError:
#     print("Invalid input! Please enter numbers for the first and second inputs.")

# Interactive user input with loop
# while True:
#     try:
#         a = input("Enter the first number (or type 'exit' to quit): ")
        
#         if a.lower() == 'exit':
#             print("Exiting the calculator. Goodbye!")
#             break

#         b = input("Enter the second number: ")
        
#         # Convert inputs to float
#         a = float(a)
#         b = float(b)

#         operation = input("Enter an operation (+, -, *, /, %, **): ")

#         result = calculate(a, b, operation)
#         print("Result:", result)

#     except ValueError:
#         print("Invalid input! Please enter valid numbers.")

