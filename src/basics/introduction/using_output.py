# We use the print() function to output data to the standard output device (screen).

print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5


# In the second 'print()' statement, we can notice that a space was added
# between the string and the value of variable a.
# This is by default, but we can change it.

# syntax of print(): print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1, 2, 3, 4)
# Output: 1 2 3 4

print(1, 2, 3, 4, sep='*')
# Output: 1*2*3*4

print(1, 2, 3, 4, sep='#', end='&\n')
# Output: 1#2#3#4&
