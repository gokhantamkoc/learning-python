# Sometimes we would like to format our output to make it look attractive.
# This can be done by using the str.format() method. This method is visible to any string object.

x, y = 5, 10

print('The value of x is {} and y is {}'.format(x, y))

# Here the curly braces {} are used as placeholders.
# We can specify the order in which it is printed by using numbers (tuple index).

print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

# We can even format strings like the old sprintf() style used in C programming language.
# We use the % operator to accomplish this.

x = 87.467656
print('The value of x is: %3.2f' % x)       # rounds the value
