# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was


number_of_lines = int(input("How many lines should the diamond have? "))
i = 0
top_lines = number_of_lines // 2 + 1
while i < top_lines:
    print((" " * (top_lines - i - 1)) + ("*" * (2 * i + 1)))
    i += 1

bottom_lines = number_of_lines // 2
i = bottom_lines
spaces = 1
while i >= 0:
    print((" " * spaces) + ("*" * (2 * i - 1)))
    i -= 1
    spaces += 1
