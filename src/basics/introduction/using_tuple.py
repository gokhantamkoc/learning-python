""" Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified. """

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10

# TypeError: 'tuple' object does not support item assignment