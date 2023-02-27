# Write a function called countLines() that takes a filename as string as a parameter
# and  returns the number of lines the file contains.
# It should return zero if it can't open the file and
# should not raise any error.

def count_lines(file_name:str) -> int:
    try:
        count = 0
        with open(file_name) as file:
            for i in file:
                count += 1
            return count
    except:
        return 0


# file_name = "vyfyiv.txt"
# file_name = "my-file.txt"
# file_name = "empty.txt"

print(count_lines(file_name))