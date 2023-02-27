# Write a program that asks for a number
# It would ask this many times to enter an integer
# If all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4


total_numbers = int(input("Give me a number: "))
numbers = []

i = 1
while i <= total_numbers:
    numbers.append(int(input("Give me an integer: ")))
    i += 1

sum = 0
for number in numbers:
    sum += number

average = sum / total_numbers

print(f"Sum of {numbers} = " + str(sum))
print(f"Average of {numbers} = " + str(average))
