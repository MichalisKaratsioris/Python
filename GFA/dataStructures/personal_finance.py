expenses = [500, 1000, 1250, 175, 800, 120]
sum = 0
for number in expenses:
    sum += number
average = sum / len(expenses)

print("How much did we spend?")
print(sum)

print("Which was our greatest expense?")
print(max(expenses))

print("Which was our cheapest spending?")
print(min(expenses))

print("What was the average amount of our spendings? (print this as a float value)")
print(average)