# - Create an array variable named `numbers` with the following content:
#   `[3, 4, 5, 6, 7]`
# - Double all the values in the array

numbers = [3, 4, 5, 6, 7]
print(numbers)
for i in range(len(numbers)):
    numbers[i] *= 2
print(numbers)
