# Python provides operations involving fractional numbers through its fractions module.

# A fraction has a numerator and a denominator, both of which are integers.
# This module has support for rational number arithmetic.

# We can create Fraction objects in various ways.

import fractions

# Output: 3/2
print(fractions.Fraction(1.5))

# Output: 5
print(fractions.Fraction(5))

# Output: 1/3
print(fractions.Fraction(1, 3))

# While creating Fraction from float, we might get some unusual results.
# This is due to the imperfect binary floating point number representation as discussed in the previous section.

# Fortunately, Fraction allows us to instantiate with string as well.
# This is the preferred options when using decimal numbers.

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))

# This datatype supports all basic operations. Here are few examples.

# Output: 2/3
print(fractions.Fraction(1, 3) + fractions.Fraction(1, 3))

# Output: 6/5
print(1 / fractions.Fraction(5, 6))

# Output: False
print(fractions.Fraction(-3, 10) > 0)

# Output: True
print(fractions.Fraction(-3, 10) < 0)
