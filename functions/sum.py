# Write a function called `sum()` that returns the sum of numbers from zero to the given parameter


def sum(upper_limit:int):
    sum = 0
    for number in range(int(upper_limit) + 1):
        sum += number
    return sum


print(sum(5))
print(sum(10))
