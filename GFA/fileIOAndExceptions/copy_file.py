# Write a function that copies the contents of a file into another file
# It should take two filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(file_to_copy:str, file_to_copy_to:str) -> bool:
    try:
        with open(file_to_copy, 'r') as file1, open(file_to_copy_to, 'w') as file2:
            for line in file1:
                file2.write(line)
        return True
    except:
        return False


copy_file("my-file.txt", "empty.txt")
