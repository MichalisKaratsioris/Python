# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

x = float(10)
y = float(10)
z = float(10)

surface = int(2 * (x * y + x * z + y * z))
volume = int(x * y * z)

print("S = " + str(surface))
print("V = " + str(volume))
