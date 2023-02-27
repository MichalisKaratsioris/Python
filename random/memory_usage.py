import sys
# In bytes
a = sys.getsizeof(0)
b = sys.getsizeof(10)
c = sys.getsizeof(1_000)
d = sys.getsizeof(1_000_000)
e = sys.getsizeof(1_000_000_000)
print("                 0: ", a, "      bytes.")
print("                10: ", b, "      bytes.")
print("             1_000: ", c, "      bytes.")
print("         1_000_000: ", d, "      bytes.")
print("     1_000_000_000: ", e, "      bytes.")

s_0 = set()
s_10 = set()
s_100 = set()
s_1_000 = set()
s_1_000_000 = set()
# s_1_000_000_000 = set()

for i in range(1, 1_000_000):
    if i <= 10:
        s_10.add(i)
        s_100.add(i)
        s_1_000.add(i)
        s_1_000_000.add(i)
    elif i <= 100:
        s_100.add(i)
        s_1_000.add(i)
        s_1_000_000.add(i)
    elif i <= 1_000:
        s_1_000.add(i)
        s_1_000_000.add(i)
    else:
        s_1_000_000.add(i)
        
# for i in range(1_000_000_000):
#     s_1_000_000_000.add(i)

print("            Set(0): ", sys.getsizeof(s_0), "     bytes.")
print("           Set(10): ", sys.getsizeof(s_10), "     bytes.")
print("          Set(100): ", sys.getsizeof(s_100), "    bytes.")
print("        Set(1,000): ", sys.getsizeof(s_1_000), "   bytes.")
print("    Set(1,000,000): ", sys.getsizeof(s_1_000_000), "bytes.")
# print("Set(1,000,000,000): ", sys.getsizeof(s_1_000_000_000), "bytes.")
