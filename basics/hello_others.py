# Greet 3 of your classmates with this program in three separate lines
# like:
#
# Hello, Esther!
# Hello, Mary!
# Hello, Joe!

names = []
i = 1
number_of_students = 3

while i <= number_of_students:
    name = input(f"What is the {i}th student's name? ")
    if not name.isdigit():
        names.append(name)
        i += 1
    else:
        print("Please, provide a valid name.")


for name in names:
    print(name)

