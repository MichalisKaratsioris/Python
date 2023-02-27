# Write a program that opens a file called "my-file.txt" and prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# it should print the following error message: "Unable to read file: my-file.txt"

try:
    file_name = "vyfyiv.txt"
    # file_name = "my-file.txt"
    # file_name = "empty.txt"
    with open(file_name) as file:
        for i in file:
            print(i, end="")
except FileNotFoundError:
    print(f"Unable to read file: {file_name}")
