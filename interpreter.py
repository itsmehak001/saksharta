# Get the math expression from the user
expression = input("Enter a math expression: ")

# Evaluate the expression and display the result
try:
    result = eval(expression)
    print("Output:", result)
except:
    print("Invalid expression!")
