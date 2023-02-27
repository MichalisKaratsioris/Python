# Create a method called decryptDoubled() that takes a filename as string as a parameter
# and it can decrypt the duplicated-chars.txt file
# Decryption is the process reversing an encryption, i.e. the process
# which converts encrypted data into its original form.
# If the file can't be opened it should return this message: File not found
# The result should be saved in the output.txt file

def decrypt_word(word:str) -> str:
    char_list = []
    for char in word:
        char_list.append(char)
    for i in range(len(char_list)-1):
        if char_list[i] == char_list[i+1]:
            char_list[i+1] = ""
    clean_word = ""
    for char in char_list:
        if char != " ":
            clean_word += char
    return clean_word


def decrypt(file_name:str):
    try:
        with open(file_name, 'r') as file1:
            clean_line = ""
            for line in file1:
                encrypted_line = line.split(" ")
                for word in encrypted_line:
                    clean_line += decrypt_word(word) + " "
            with open("output.txt", 'w') as file2:
                file2.write(clean_line)
    except:
        print("File not found")


decrypt("duplicated-chars.txt")

