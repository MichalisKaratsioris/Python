# Create a method that decrypts reversed-lines.txt


def reverse_word(word:str) -> str:
    result = ""
    char_list = []
    for char in word:
        char_list.append(char)
    for i in range(len(char_list)):
        char_list[i] = word[len(char_list) - 1 - i]
    for i in range(len(char_list)):
        result += char_list[i]
    return result


def decrypt(file_name):
    try:
        with open(file_name, 'r') as file1:
            clean_line = ""
            swap = ""
            for line in file1:
                encrypted_line = line.split(" ")
                for i in range(int(len(encrypted_line)/2)):
                    swap = encrypted_line[i]
                    encrypted_line[i] = encrypted_line[len(encrypted_line) - 1 - i]
                    encrypted_line[len(encrypted_line) - 1 - i] = swap
                for word in encrypted_line:
                    clean_line += reverse_word(word) + " "
            with open("output.txt", 'w') as file2:
                file2.write(clean_line)
    except:
        print("File not found")


decrypt("reversed-lines.txt")