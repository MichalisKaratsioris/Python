a = 24
output1 = 0
# if a is even increment output1 by one
if (a % 2) == 0:
    output1 += 1

print(output1)




b = 13
output2 = ""
# if b is between 10 and 20 set output2 to "Sweet!"
# if less than 10 set output2 to "Less!",
# if more than 20 set output2 to "More!"

if 10 < b < 20:
    output2 = "Sweet!"
elif b < 10:
    output2 = "Less!"
else:
    output2 = "More!"


print(output2)



c = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

if (credits >= 50) and (not is_bonus):
    c -= 2
elif (credits < 50) and (not is_bonus):
    c -= 1
elif is_bonus:
    pass

print(c)




d = 8
time = 120
output3 = ""
# if d is dividable by 4
# and time is not more than 200
# set output3 to "check"
# if time is more than 200
# set output3 to "Time out"
# otherwise set output3 to "Run Forest Run!"

if (d % 4 == 0) and (time <= 200):
    output3 = "check"
elif time > 200:
    output3 = "Time out"
else:
    output3 = "Run Forest Run!"

print(output3)
