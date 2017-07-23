# Operators are special symbols in Python that carry out arithmetic or logical computation.
# The value that the operator operates on is called the operand.

# arithmetic operators

x = 15
y = 4

# addition
print('x + y =', x + y)

# substraction
print('x - y =', x - y)

# multiplication
print('x * y =', x * y)

# division
print('x / y =', x / y)

# modulo
print('x // y =', x // y)

# exponent => 15^4
print('x ** y =', x ** y)

print()

# comparison operators

x = 10
y = 12

# Output: x > y is False
print('x > y  is', x > y)

# Output: x < y is True
print('x < y  is', x < y)

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)

print()

# logical operators

x = True
y = False

# Output: x and y is False
print('x and y is', x and y)

# Output: x or y is True
print('x or y is', x or y)

# Output: not x is False
print('not x is', not x)

print()

# bitwise operators

# Bitwise operators act on operands as if they were string of binary digits.
# It operates bit by bit, hence the name.

# x is 10 (Binary: 0000 1010), y is 4(Binary: 0000 0100)

# Operator      Meaning                 Example
# &             Bitwise AND             x & y = 0 (0000 0000)
# |             Bitwise OR              x | y = 14 (0000 1110)
# ~             Bitwise NOT             ~x = -11 (1111 0101)        # All bits are inverted.
# ^             Bitwise XOR 	        x ^ y = 10 (0000 1110)
# >>            Bitwise Right Shift 	x >> 2 = 2 (0000 0010)
# <<            Bitwise Left Shift      x << 2 = 40 (0010 1000)

x = 10
y = 4

print(x & y)            # Output: 0
print(x | y)            # Output: 14
print(~x)               # Output: -11
print(x ^ y)            # Output: 10
print(x >> 2)           # Output: 2
print(x << 2)           # Output: 40

print()

# assignment operators

# Assignment operators are used in Python to assign values to variables.
# a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
# There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same.
# It is equivalent to a = a + 5.

# Operator          Example         Equivalent to
# =                 x = 5
# +=                x += 5          x = x + 5
# -=                x -= 5          x = x - 5
# *=                x *= 5          x = x * 5
# /=                x /= 5          x = x / 5
# %=                x %= 5          x = x % 5
# //=               x //= 5         x = x // 5
# **=               x **= 5         x = x ** 5
# &=                x &= 5          x = x & 5
# |=                x |= 5          x = x | 5
# ^=                x ^= 5          x = x ^ 5
# >>=               x >>= 5         x = x >> 5
# <<=               x <<= 5         x = x << 5

# special operators

# Python language offers some special type of operators like identity operator or the membership operator.

## identity operators

# 'is' and 'is not' are the identity operators of Python. They are used to check if two variables are located on the same memory place.

# Let's assume x = True

# Operator	Meaning							Example
#  is		True if the variables refer to the same object		x is True
#  is not	True if the operands do not refer to the same object	x is not True

x = True

print(x is True)
print(x is not True)

x1 = 5
y1 = 5
x2 = 'hello'
y2 = 'hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x3 is y3)  # x3 and y3 are lists. They are equal but do not refer to the same object.

## membership operators

# Operator	Meaning
#  in		True if value/variable is found in the sequence		5 in x
#  not in	True if value/variable is not found in the sequence	5 not in x

# Important note: In dictionary you can only test if the key is present, whereas you cannot test if a value is present.

x = 'Hello World'
y = {1: 'a', 2: 'b'}

print('H' in x)
print(1 in y)
print('a' in y)


