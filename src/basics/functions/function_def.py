# 1. Keyword def marks the start of function header.
# 2. A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
# 3. Parameters (arguments) through which we pass values to a function. They are optional.
# 4. A colon (:) to mark the end of function header.
# 5. Optional documentation string (docstring) to describe what the function does.
# 6. One or more valid python statements that make up the function body.
#    Statements must have same indentation level (usually 4 spaces).
# 7. An optional return statement to return a value from the function.


def greet(name):
    """
    This function greets to
    the person passed in as
    parameter
    """

    print('Hello', name)


greet('Gokhan')
print(greet.__doc__)


def absolute_value(num):
    """
    This function will return the absolute value of the parameter.
    :param num
    :return integer value
    """
    if num >= 0:
        return num
    else:
        return -num

print(str(absolute_value(-203)))
print(absolute_value.__doc__)


# Scope of a variable is the portion of a program where the variable is recognized.
# Parameters and variables defined inside a function is not visible from outside.
# Hence, they have a local scope.

# Lifetime of a variable is the period throughout which the variable exits in the memory.
# The lifetime of variables inside a function is as long as the function executes.
# They are destroyed once we return from the function.
# Hence, a function does not remember the value of a variable from its previous calls.
# Here is an example to illustrate the scope of a variable inside a function.

def my_func():
    x = 10
    print("Value inside function:", x)

x = 20
my_func()
print("Value outside function:", x)

# two types of functions
# 1. Built-in functions: functions defined in Python
# 2. User-defined functions: functions defined by users.

'''
Test
'''

_test = 4

print(_test)
