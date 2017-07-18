# Set is a collection of unique items.
# Set is defined by values separated by comma inside braces { }.
# Items in a set are not ordered.

a = {5, 2, 3, 1, 4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

a = {1, 2, 2, 3, 3, 3}  # Python will eliminate duplicates.

print(a)

# Since set is an unordered collection, array operations will not work
print(a[1])