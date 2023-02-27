# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was

number_of_lines = int(input("How many lines should the pyramid have? "))

# printing first line
i = 1
while i < number_of_lines:
    print("%", end="")
    i += 1
else:
    print("%")

# printing side lines
i = 1
while i <= (number_of_lines - 2):
    print("%" + " " * (number_of_lines - 2) + "%")
    i += 1

# printing bottom line
i = 1
while i <= number_of_lines:
    print("%", end="")
    i += 1