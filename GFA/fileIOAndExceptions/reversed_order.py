# Create a method that decrypts reversed-order.txt


def decrypt(file_name):
    try:
        with open(file_name, 'r') as file1:
            clean_line = ""
            encrypted_line = []
            for line in file1:
                encrypted_line.append(line)
            for i in range(int(len(encrypted_line))):
                clean_line += encrypted_line[len(encrypted_line) - 1 - i]
                clean_line += "\n"
            with open("output.txt", 'w') as file2:
                file2.write(clean_line)
    except:
        print("File not found")


decrypt("reversed-order.txt")