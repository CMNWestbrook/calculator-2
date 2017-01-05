"""calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    user_input = raw_input("> ")
    tokens = user_input.split()
    arg3 = ["+", "-", "*", "/", "pow", "mod"]
    arg2 = ["square", "cube"]
    if ((tokens[0] in arg3 and len(tokens) != 3) or
        (tokens[0] in arg2 and len(tokens) != 2)):
        print("Wrong number of arguments")
        continue

    if tokens[0] == "+":
        print(add(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "-":
        print(subtract(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "*":
        print(multiply(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "/":
        print(divide(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "square":
        print(square(int(tokens[1])))
    elif tokens[0] == "cube":
        print(cube(int(tokens[1])))
    elif tokens[0] == "pow":
        print(power(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "mod":
        print(mod(int(tokens[1]), int(tokens[2])))
    elif tokens[0].lower() == "q":
        break
    else:
        print("I don\'t understand")
