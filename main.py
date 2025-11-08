# Get two numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b if b != 0 else 'Cannot divide by zero'}")
