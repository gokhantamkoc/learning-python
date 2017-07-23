# Up till now, our programs were static.
# The value of variables were defined or hard coded into the source code.

# To allow flexibility we might want to take the input from the user.
# In Python, we have the input() function to allow this. The syntax for input() is

num = input('Enter a number:\n')

print(num)
print(type(num))

# The type of num is String. In order to use the variable in numeric operations,
# you must convert it to a numeric type.

print(int(num))
print(float(num))

print(eval('2+3'))
print(int('2+3'))
