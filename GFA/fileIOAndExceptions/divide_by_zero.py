# Create a function that divides number 10
# by a number that's passed as a paramater and prints the result.
# It should print "fail" if the parameter is 0


def divide_by_zero(number:int):
    if number != 0:
        return 10 / number
    return "fail"


print(divide_by_zero(0))
print(divide_by_zero(10))
print(divide_by_zero(5))
