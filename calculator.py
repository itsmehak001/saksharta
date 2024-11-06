def calculator():
    """This function performs basic calculator operations."""

    # Get input from the user
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the calculation based on the operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Division by zero is not allowed!"
        else:
            result = num1 / num2
    else:
        return "Invalid operator!"

    # Display the result
    print("Result: ", result)

# Call the calculator function
calculator()
