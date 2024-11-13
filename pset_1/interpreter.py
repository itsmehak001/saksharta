# get user input 
expression = input("Expression: ")
# convert this into variables 
x, y, z = expression.split(" ")
# change type of variables x and z to float 
new_x = float(x)
new_z = float(z)
# calculate the result
if y == "+":
    result = new_x + new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    results = new_x / new_z
print(result)