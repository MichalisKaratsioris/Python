# Create a function called 'reverse()' which takes a string as a parameter
# Pass the toBeReversed variable to this method to check if it works well

def reverse(string:str):
    result = ""
    for i in range(len(string)):
        result += string[len(string) - 1 - i]
    return result


toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
print(reverse(toBeReversed))
