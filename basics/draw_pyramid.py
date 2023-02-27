# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

number_of_lines = int(input("How many lines should the pyramid have? "))

i = 0
while i < number_of_lines:
    print((" " * (number_of_lines - i - 1)) + ("*" * (2 * i + 1)))
    i += 1