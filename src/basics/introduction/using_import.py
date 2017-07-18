# When our program grows bigger, it is a good idea to break it into different modules.
# A module is a file containing Python definitions and statements.
# Python modules have a filename and end with the extension '.py'.

import math                 # All the definitions inside math module are available in our scope.
from math import pi         # If you want to use a specific attribute or function use 'from'.
import sys                  #

print(math.pi)
print(pi)
print(sys.path)

