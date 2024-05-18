
# Define a function that divides two numbers
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Oops! An error occurred: Division by zero")
        return None
    else:
        return result

# Ask the user to input two numbers and perform the division
while True:
    x = input("Enter the numerator: ")
    y = input("Enter the denominator: ")
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    result = divide(x, y)
    if result is not None:
        print(f"The result is {result}")
        
    choice = input("Do you want to perform another division? (y/n): ")
    if choice.lower() == 'n':
        break
