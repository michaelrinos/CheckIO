"""
 The greatest common divisor (GCD), also known as the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.

You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers.

Input: An arbitrary number of positive integers.

Output: The greatest common divisor as an integer.

Example:

great_common_divisor(6, 4) == 2
great_common_divisor(2, 4, 8) == 2

Precondition:
1 < len(args) ≤ 10
all(0 < x ≤ 2 ** 32 for x in args)
"""

from functools import reduce
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def greatest_common_divisor(*args):
    if len(args) == 2:
        return gcd(args[0],args[1])
    
    else:
        return reduce(gcd,args)
    
        
    return temp

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

