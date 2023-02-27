# Write a function that is able to manipulate a file
# by writing your name into it as a single line.
# The file should be named "my-file.txt".
# In case the program is unable to write the file,
# it should print the following error message: "Unable to write file: my-file.txt"

def write_single_line(file_name:str):
    try:
        # with open(file_name, 'w') as file:
        #     file.write("Shiushin\n")
        #     file.write("Michalis Karatsioris\n")
        with open(file_name, 'a') as file:
            file.write("Shiushinnnnnnnn\n")
            file.write("Michalis Karatsiorisssssss\n")
    except:
        print(f"Unable to write file: {file_name}")


write_single_line("my-file.txt")