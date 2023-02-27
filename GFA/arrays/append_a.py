# - Create a variable named `animals`
#   with the following content:
#   `["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr", "gorill",
#    "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "pirahn"]`
#
# - Add all elements an `"a"` at the end

animals = ["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr", "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "pirahn"]
print(animals)
i = 0
while i < len(animals):
    animals[i] += "a"
    i += 1

print(animals)
