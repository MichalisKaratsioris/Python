from math import floor


def significant_arithmetic_rounding(n, d):
    '''
    This function takes a floating point number and the no. of significant digit d, perform significant digits
    arithmetic rounding and returns the floating point number after rounding
    '''
    if n == 0:
        return 0
    else:
        # Checking whether the no. is negative or positive. If it is negative we will take the absolute value of it and proceed
        neg_flag = 0
        if n < 0:
            neg_flag = 1
            n = abs(n)

        n1 = n
        # Counting the no. of digits to the left of the decimal point in the no.
        ld = 0
        while (n1 >= 1):
            n1 /= 10
            ld += 1

        n1 = n
        # Counting the no. of zeros to the right of the decimal point and before the first significant digit in the no.
        z = 0
        if ld == 0:
            while (n1 <= 0.1):
                n1 *= 10
                z += 1

        n1 = n
        # No. of digits to be considered after decimal for rounding
        rd = (d - ld) + z
        n1 *= 10 ** rd

        # Increase by 0.5 and take the floor value for rounding
        n1 = floor(n1 + 0.5)
        # Placing the decimal point at proper position
        n1 /= 10 ** rd
        # If the original number is negative then make it negative
        if neg_flag == 1:
            n1 = 0 - n1

        return n1


print(significant_arithmetic_rounding(3.595758493, 1))
print(significant_arithmetic_rounding(3.595758493, 2))
print(significant_arithmetic_rounding(3.595758493, 3))
print(significant_arithmetic_rounding(3.595758493, 4))
print(significant_arithmetic_rounding(3.595758493, 5))
print(significant_arithmetic_rounding(3.595758493, 6))
