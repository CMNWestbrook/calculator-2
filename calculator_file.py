"""calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

file_name = "numbers.txt"
with open(file_name) as f:
    tokens = f.readlines()
    print(tokens)


arg3 = ["+", "-", "*", "/", "pow", "mod"]
arg2 = ["square", "cube"]
if ((tokens[0] in arg3 and len(tokens) < 3) or
    (tokens[0] in arg2 and len(tokens) != 2)):
    print("Wrong number of arguments. Check your file")
else:

    if tokens[0] == "+":
        print('{0:.2f}'.format(reduce((lambda x,y: add(int(x), int(y))), tokens[1:])))
    elif tokens[0] == "-":
        print('{0:.2f}'.format(reduce((lambda x,y: subtract(int(x), int(y))), tokens[1:])))
    elif tokens[0] == "*":
        print('{0:.2f}'.format(reduce((lambda x,y: multiply(int(x), int(y))), tokens[1:])))
    elif tokens[0] == "/":
        print('{0:.2f}'.format(reduce((lambda x,y: divide(int(x), int(y))), tokens[1:])))
    elif tokens[0] == "square":
        print('{0:.2f}'.format(square(int(tokens[1]))))
    elif tokens[0] == "cube":
        print('{0:.2f}'.format(cube(int(tokens[1]))))
    elif tokens[0] == "pow":
        print('{0:.2f}'.format(reduce((lambda x,y: power(int(x), int(y))), tokens[1:])))
    elif tokens[0] == "mod":
        print('{0:.2f}'.format(reduce((lambda x,y: mod(int(x), int(y))), tokens[1:])))
    else:
        print("I don\'t understand. Check your file")

f.close()
