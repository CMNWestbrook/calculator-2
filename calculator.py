from arithmetic import *


def calculator():
    """calculator.py

    Using our arithmetic.py file from Exercise02, create the
    calculator program yourself in this file.
    """

    while True:
        user_input = raw_input("> ")
        tokens = user_input.split(" ")
        if tokens[0] == "+":
            if len(tokens) < 3:
                print(" Not Enough Numbers")
            else:
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
            return
        else:
            print("I don\'t understand")

calculator()
