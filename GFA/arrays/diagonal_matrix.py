# - Create a two dimensional list dynamically with the following content.
#   Note that a two dimensional list is often called matrix if every
#   internal list has the same length.
#   Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
#   Its length should depend on a variable
#
# - Print this two dimensional list to the output


n = int(input("How many rows and columns should the matrix have? "))

matrix = []
i = 0
while i < n:
    row = []
    j = 0
    while j < n:
        row.append(0)
        j += 1
    row[i] = 1
    matrix.append(row)
    i += 1
for row in matrix:
    print(row)
