# Python supports integers, floating point numbers and complex numbers.
# They are defined as int, float and complex class in Python.

# Integers and floating points are separated by the presence or absence of a decimal point.
# 5 is integer whereas 5.0 is a floating point number.

# Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

a = 5

# Output: <class 'int'>
print(type(a))

# Output: <class 'float'>
print(type(5.0))

# Output: (8+3j)
c = 5 + 3j
print(c + 3 + 1j)

# Output: True
print(isinstance(c, complex))

# While integers can be of any length, a floating point number is
# accurate only up to 15 decimal places (the 16th place is inaccurate).

# Numbers we deal with everyday are decimal (base 10) number system. But computer programmers
# (generally embedded programmer) need to work with binary (base 2), hexadecimal (base 16) and
# octal (base 8) number systems.

# In Python, we can represent these numbers by appropriately placing a prefix before that number.
# Following table lists these prefix.

# Number System             Prefix
# Binary                    '0b' or '0B'
# Octal                     '0o' or '0O'
# Hexadecimal               '0x' or '0X'

# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15),
