map = {}
print(len(map) == 0)
map[97] = 'a'
map[98] = 'b'
map[99] = 'c'
map[65] = 'A'
map[66] = 'B'
map[67] = 'C'
print(map.keys())
print(map.values())
map[68] = 'D'
print(len(map))
print(map[99])
print(map.pop(97))
print(100 in map.keys())
map.clear()
print(len(map))
