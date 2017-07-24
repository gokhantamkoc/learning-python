import example                          # basic usage of import
import example as ex                    # import with renaming
from example import what_a_variable
from example import *
import sys

print(example.add(5, 6))
print(ex.add(101, 2))

# import with from keyword

print(what_a_variable)

# With using *(star) import we included all definitions visible to other classes.
# This makes all names except those beginning with an underscore,
# visible in our scope.

# Importing everything with the asterisk (*) symbol is not a good programming practice.
# This can lead to duplicate definitions for an identifier. It also decreases the readability of our code.

print(add(105, 789))

# While importing a module, Python looks at several places.
# Interpreter first looks for a built-in module then (if not found) ,
# into a list of directories defined in sys.path. The search is in this order.

for path in sys.path:
    print(path)


# reloading a module

# The Python interpreter imports a module only once during a session.
# This makes things more efficient.
# Here is an example to show how this works.

# This module shows the effect of
#  multiple imports and reload

print("This code got executed")

# We can see that our code got executed only once. This goes to say that our module was imported only once.
# Now if our module changed during the course of the program, we would have to reload it.
# One way to do this is to restart the interpreter.
# But this does not help much.

# Python provides a neat way of doing this. We can use the reload() function inside the imp module to reload a module.
# This is how its done.

# >>> import imp
# >>> import modder
# This code got executed
# >>> import modder
# >>> imp.reload(modder)
# This code got executed
# <module 'modder' from '.\\modder.py'>

# dir() function
# We can use the dir() function to find out names that are defined inside a module.

for item in dir(example):
    print(item)

for item in dir(sys):
    print(item)


