# In Python programming, a list is created by placing all the items (elements) inside a square bracket [ ],
# separated by commas.

# It can have any number of items and they may be of different types (integer, float, string etc.).

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list)

# accessing items in a list using index

# We can use the index operator [] to access an item in a list. Index starts from 0.
# So, a list having 10 elements will have index from 0 to 9.

# Trying to access an element other that this will raise an IndexError. The index must be an integer.
# We can't use float or other types, this will result into TypeError.

my_list = ['p', 'r', 'o', 'b', 'e']
# Output: p
print(my_list[0])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0] :-D

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing

# Output: a
print(n_list[0][1])

# Output: 5
print(n_list[1][3])

# negative indexing

my_list = ['p', 'r', 'o', 'b', 'e']

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])

# slicing lists

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# visualization of my_list
#   p   r   o   g   r   a   m   i   z
#   0   1   2   3   4   5   6   7   8
#  -9  -8  -7  -6  -5  -4  -3  -2  -1

# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# updating the elements of a list

# List are mutable, meaning, their elements can be changed unlike "string" or "tuple".

# We can use assignment operator (=) to change an item or a range of items.

# mistake values
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

# Output: [1, 3, 5, 7]
print(odd)

# We can add one item to a list using append() method or add several items using extend() method.

odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)

# We can also use + operator to combine two lists. This is also called concatenation.

# The * operator repeats a list for the given number of times.

odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

# Output: ["re", "re", "re"]
print(["re"] * 3)

# Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items
# by squeezing it into an empty slice of a list.

odd = [1, 9]
odd.insert(1, 3)

# Output: [1, 3, 9]
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)

# removing items from a list

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']
print(my_list)

# delete multiple items
del my_list[1:5]

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list

# print(my_list) # Error: List not defined

# We can use remove() method to remove the given item or pop() method to remove an item at the given index.

# The pop() method removes and returns the last item if index is not provided.
# This helps us implement lists as stacks (first in, last out data structure).

# We can also use the clear() method to empty a list.

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)

# In Python, deleting items can be done with assigning empty list to a slice

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

my_list[2:5] = []

print(my_list)

my_list[1:2] = []

print(my_list)

# list methods

# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

try:
    my_list.index('P    ')
except ValueError:
    print('P is not in my_list')
else:
    print('P is in my_list')

# list comprehension

# list comprehension is an elegant and concise way to create new list from an existing list in Python.

pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

pow2 = []

# you can do the same with a for loop

for x in range(10):
    pow2.append(2 ** x)

print(pow2)

# A list comprehension can optionally contain more for or if statements.
# An optional if statement can filter out items for the new list. Here are some examples.

pow2 = [2 ** x for x in range(10) if (2 ** x) > 5]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)

concat = [x+y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
print(concat)

# list membership test

# Python has the ability to test if an item is a member of a list. The 'in' keyword is used for testing list membership.

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)

for fruit in ['apple', 'banana', 'mango']:
    print("I like", fruit)

# built-in functions


# all() function: takes one parameter which will be a list and returns boolean value.

# If the boolean value is true, then all items are true(items are not 0(zero), False and None)
# If the boolean value is false, one of the item is false(one of them is False, 0(zero) or None)

# all values are true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# Important: empty string is true
s = ''
print(all(s))

print((1, 2) + (3, 4))
