import math


def to_precision(x, p):
    """
    returns a string representation of x formatted with a precision of p
    """

    x = float(x)

    if x == 0.:
        return "0." + "0"*(p-1)

    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - p + 1)
    n = math.floor(x/tens)

    if n < math.pow(10, p - 1):
        e = e -1
        tens = math.pow(10, e - p+1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens -x):
        n = n + 1

    if n >= math.pow(10,p):
        n = n / 10.
        e = e + 1

    m = "%.*g" % (p, n)

    if e < -2 or e >= p:
        out.append(m[0])
        if p > 1:
            out.append(".")
            out.extend(m[1:p])
        out.append('e')
        if e > 0:
            out.append("+")
        out.append(str(e))
    elif e == (p -1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e+1])
        if e+1 < len(m):
            out.append(".")
            out.extend(m[e+1:])
    else:
        out.append("0.")
        out.extend(["0"]*-(e+1))
        out.append(m)

    return "".join(out)


print(to_precision(12.3456789000, 1))
print(to_precision(12.3456789000, 2))
print(to_precision(12.3456789000, 3))
print(to_precision(12.3456789000, 4))
print(to_precision(12.3456789000, 5))
print(to_precision(12.3456789000, 6))
print(to_precision(12.3456789000, 7))
print(to_precision(12.3456789000, 8))
print(to_precision(12.3456789000, 9))
print(to_precision(12.3456789000, 10))
print(to_precision(12.3456789000, 11))
print(to_precision(12.3456789000, 12))
print(to_precision(12.3456789000, 13))
print(to_precision(12.3456789000, 14))