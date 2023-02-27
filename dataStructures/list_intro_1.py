names = []
print(len(names))

names.append("William")
print(len(names) == 0)

names.append("John")
names.append("Amanda")
print(len(names))

print(names[2])

for name in names:
    print(name)

i = 1
for name in names:
    print(f"{i}. " + name)
    i += 1

names.remove(names[1])
for i in range(len(names)):
    print(names[len(names) - 1 - i])

names.clear()
print(len(names))