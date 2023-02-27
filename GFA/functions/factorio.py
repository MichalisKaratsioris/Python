# - Create a function called `calculateFactorial()`
#   that returns the factorial of its input

def calculateFactorial(number:int):
    if (int(number) != 0) or (int(number) == 1):
        fact = 1
        for number in range(1, int(number)+1):
            fact *= int(number)
        return fact
    return 1

print(calculateFactorial(0))
print(calculateFactorial(1))
print(calculateFactorial(3))
print(calculateFactorial(5))
