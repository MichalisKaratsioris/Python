# Modify this program to greet you instead of the World!
# print("Hello, World!")

name = input("What is your name? ")
if not name.isdigit():
    print(f"Hello {name}")
else:
    print("Please, provide a valid name.")