# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

numbers = []

i = 1
while i <= 5:
    numbers.append(int(input("Give me an integer: ")))
    i += 1

sum = 0
for number in numbers:
    sum += number

average = sum / len(numbers)

print(f"Sum of {numbers} = " + str(sum))
print(f"Average of {numbers} = " + str(average))