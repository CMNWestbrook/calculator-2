"""calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    file_name = "numbers.txt"
    try:
        with open(file_name) as f:
            tokens = f.readlines()
        f.close()
    except (OSError, IOError) as e:
        print("The file numbers.txt doesn\'t exist!")
        return

    tokens[0] = tokens[0].rstrip()

    arg3 = ["+", "-", "*", "/", "pow", "mod"]
    arg2 = ["square", "cube"]

    if ((tokens[0] in arg3 and len(tokens) < 3) or
        (tokens[0] in arg2 and len(tokens) != 2)):
        print("Wrong number of arguments. Check your file")
    else:
        result = open("result.txt","w")
        if tokens[0] == "+":
            result.write('{0:.2f}'.format(reduce((lambda x,y: add(int(x), int(y))), tokens[1:])))
        elif tokens[0] == "-":
            result.write('{0:.2f}'.format(reduce((lambda x,y: subtract(int(x), int(y))), tokens[1:])))
        elif tokens[0] == "*":
            result.write('{0:.2f}'.format(reduce((lambda x,y: multiply(int(x), int(y))), tokens[1:])))
        elif tokens[0] == "/":
            result.write('{0:.2f}'.format(reduce((lambda x,y: divide(float(x), float(y))), tokens[1:])))
        elif tokens[0] == "square":
            result.write('{0:.2f}'.format(square(int(tokens[1]))))
        elif tokens[0] == "cube":
            result.write('{0:.2f}'.format(cube(int(tokens[1]))))
        elif tokens[0] == "pow":
            result.write('{0:.2f}'.format(reduce((lambda x,y: power(int(x), int(y))), tokens[1:])))
        elif tokens[0] == "mod":
            result.write('{0:.2f}'.format(reduce((lambda x,y: mod(int(x), int(y))), tokens[1:])))
        else:
            print("I don\'t understand. Check your file")

    result.close()

calculator()
