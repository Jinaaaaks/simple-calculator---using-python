# Simple calculator

# Addition function
def addition(num1, num2):
    "This function calculates the addition of two numbers"
    # Processing
    adtotal = num1 + num2  # Adding the 2 numbers
    return adtotal

# Subtraction function
def subtract(num1, num2):
    "This function calculates the subtraction of two numbers"
    # Processing
    subtotal = num1 - num2  # Subtract num2 from num1
    return subtotal
    
# Multiplication function
def multiply(num1, num2):
    "This function calculates the multiplication of two numbers"
    # Processing
    multi_value = num1 * num2  # Multiply the two values
    return multi_value

# Division function
def division(num1, num2):
    "This function calculates the division of two numbers"
    # Processing
    divi_value = num1 / num2
    return divi_value

# Power of a number
def power_number(num1, exponent):
    "This function calculates the power of a number"
    # Processing
    power = num1 ** exponent
    return power

# - - - Main Program Area - - - #

# Initialize variables
adtotal = 0
subtotal = 0
multi_value = 0
divi_value = 0
power = 0

print("- - - Main Program - - -")

# Main program to interact with the user
print("Welcome to the Simple Calculator!")
print("Please choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")

choice = input("Enter the number of the operation you want to perform (1/2/3/4/5): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter the first number: "))
    if choice != '5':
        num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("The result of addition is: ", addition(num1, num2))
    elif choice == '2':
        print("The result of subtraction is: ", subtract(num1, num2))
    elif choice == '3':
        print("The result of multiplication is: ", multiply(num1, num2))
    elif choice == '4':
        print("The result of division is: ", division(num1, num2))
    elif choice == '5':
        exponent = float(input("Enter the exponent: "))
        print("The result of power is: ", power_number(num1, exponent))
else:
    print("Invalid choice. Please restart the program and choose a valid operation.")
