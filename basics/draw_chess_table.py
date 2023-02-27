# Crate a program that draws a chess table like this
#
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %

for i in range(8):
    for j in range(8):
        if ((i + j) % 2 == 0):
            print("%", end="")
        else:
            print(" ", end="")
    print("")