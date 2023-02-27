map = {
    "978-1-60309-452-8": "A Letter to Jo",
    "978-1-60309-459-7": "Lupus",
    "978-1-60309-444-3": "Red Panda and Moon Bear",
    "978-1-60309-461-0": "The Lab"
}

for k, v in map.items():
    print(f"{v} (ISBN: {k})")

del map["978-1-60309-444-3"]

for k, v in map.items():
    if v == "The Lab":
        del map[k]
        break

map["978-1-60309-450-4"] = "They Called Us Enemy"
map["978-1-60309-453-5"] = "Why Did We Trust Him?"

print("478-0-61159-424-8" in map.values())
print(map["978-1-60309-453-5"])

# print(map)
