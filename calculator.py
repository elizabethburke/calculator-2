"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input = raw_input()
    tokens = input.split(" ")

    if tokens[0] == 'q':
        break
    elif tokens[0] == '+':
        current_sum = 0
        for num in tokens[1:]:
            current_sum = add(current_sum, float(num))
        print current_sum
    elif tokens[0] == '-':
        print subtract(float (tokens[1]), float (tokens[2]))
    elif tokens[0] == '*':
        print multiply(float (tokens[1]), float (tokens[2]))
    elif tokens[0] == '/':
        print divide(float (tokens[1]), float (tokens[2]))
    elif tokens[0] == 'square':
        print square(float (tokens[1]))
    elif tokens[0] == 'cube':
        print cube(float (tokens[1]))
    elif tokens[0] == 'pow':
        print power(float (tokens[1]), float (tokens[2]))
    elif tokens[0] == 'mod':
        print mod(float (tokens[1]), float (tokens[2]))