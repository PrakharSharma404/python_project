import math

def square_root():
    x = float(input("Enter a number: "))
    if x < 0:
        print("Square root of a negative number is not defined in real numbers.")
    else:
        print(f"√{x} = {math.sqrt(x)}")

def factorial():
    x = int(input("Enter a non-negative integer: "))
    if x < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"{x}! = {math.factorial(x)}")

def natural_log():
    x = float(input("Enter a positive number: "))
    if x <= 0:
        print("Natural logarithm is not defined for zero or negative numbers.")
    else:
        print(f"ln({x}) = {math.log(x)}")

def power():
    x = float(input("Enter the base (integer or float): ")) if '.' in input("Enter the base: ") else int(input("Enter the base: "))
    b = float(input("Enter the exponent (integer or float): ")) if '.' in input("Enter the exponent: ") else int(input("Enter the exponent: "))
    print(f"{x}^{b} = {math.pow(x, b)}")

def calculator():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power Function")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            square_root()
        elif choice == '2':
            factorial()
        elif choice == '3':
            natural_log()
        elif choice == '4':
            power()
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator()
