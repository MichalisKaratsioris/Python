# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

# number of chickens
x = int(input("Give me an integer: "))
# number of pigs
y = int(input("Give me another integer: "))

total_legs = 2 * x + 4 * y
print(f"There are {total_legs} in the farm")

