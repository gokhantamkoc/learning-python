# Up until now functions had fixed number of arguments.
# In Python there are other ways to define a function which can take variable number of arguments.

# default arguments

# Function arguments can have default values in Python.

# We can provide a default value to an argument by using the assignment operator (=). Here is an example.


def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

# keyword arguments

# When we call a function with some values, these values get assigned to the arguments according to their position.

# Python allows functions to be called using keyword arguments.
# When we call functions in this way, the order (position) of the arguments can be changed.
# Following calls to the above function are all valid and produce the same result.

greet(name="Bruce", msg="How do you do?")
greet(msg="How do you do?", name="Bruce")
greet("Bruce", msg="How do you do?")


# greet(msg="How do you do?", "Bruce")                # you can not put positional argument after keyword argument

# arbitrary arguments

# Sometimes, we do not know in advance the number of arguments that will be passed into a function.
# Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.

# In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument.
# Here is an example.

def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John", "Sucker")
