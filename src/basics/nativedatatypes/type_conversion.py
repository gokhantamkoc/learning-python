from _decimal import Decimal as D

# We can convert one type of number into another. This is also known as coercion.

# Operations like addition, subtraction coerce integer to float implicitly (automatically),
# if one of the operand is float.

res = 2 + 5.0
print(res)

# We can see above that 2 (integer) is coerced into 2.0 (float) for addition and
# the result is also a floating point number.

# We can also use built-in functions like int(), float() and complex() to convert between types explicitly.
# These function can even convert from strings.

int_res = int(2.8)      # the float will be truncated when converting to int. DATA LOSS MAY OCCUR. BE CAREFUL
float_res = float(5)    # the integer will be converted to float. NO DATA LOSS. SAFE

print(int_res)
print(float_res)

# int_res = int('2.4')    # invalid literal for int() with base 10: '2.4'
# int_res = int(2 + 4j)   # CANNOT convert to int

# Python built-in class float performs some calculations that might amaze us. We all know that the
# sum of 1.1 and 2.2 is 3.3, but Python seems to disagree.

print((1.1 + 2.2) == 3.3)

# It turns out that floating-point numbers are implemented in computer hardware as binary fractions, as
# computer only understands binary (0 and 1). Due to this reason, most of the decimal fractions we know,
# cannot be accurately stored in our computer.

# Let's take an example. We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333...
# which is infinitely long, and we can only approximate it.

# Turns out decimal fraction 0.1 will result into an infinitely long binary fraction of 0.000110011001100110011...
# and our computer only stores a finite number of it.

# This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware
# and not an error in Python.

print(1.1 + 2.2)

# To overcome this issue, we can use decimal module that comes with Python. While floating point numbers have
# precision up to 15 decimal places, the decimal module has user settable precision.

# Output: 0.1
print(0.1)

# Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(D(0.1))

# This module is used when we want to carry out decimal calculations like we learned in school.
# It also preserves significance. We know 25.50 kg is more accurate than 25.5 kg as it has
# two significant decimal places compared to one.

# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))

# Notice the trailing zeroes in the above example.

# We might ask, why not implement Decimal every time, instead of float? The main reason is efficiency.
# Floating point operations are carried out must faster than Decimal operations.

# We generally use Decimal in the following cases.

# When we are making financial applications that need exact decimal representation.
# When we want to control the level of precision required.
# When we want to implement the notion of significant decimal places.
# When we want the operations to be carried out like we did at school

