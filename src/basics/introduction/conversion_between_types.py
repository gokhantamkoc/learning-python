# We can convert between different data types by using different type
# conversion functions like int(), float(), str() etc.

# conversion from integer to float

number = 5
f = float(number)

print(f)

# conversion from string to float

string_value = '5.8'
f = float(string_value)     # Conversion to and from string must contain compatible values.

print(f)

# conversion from float to integer

floating_number = 4.8
t = int(floating_number)    # Python will truncate the value

print(t)

# conversion from list to set

a = [1, 2, 5, 90, 21, 90, 2]
b = set(a)

print('conversion from list to set:', str(b))

# conversion to tuple

c = tuple(a)                # conversion from list to tuple
d = tuple(b)                # conversion from set to tuple

print('conversion from list to tuple:', str(c))
print('conversion from set to tuple: ', str(d))

# conversion to dictionary... To convert to dictionary, each element must be a pair.

l = [(1, 'Dev'), (2, 'Stage')]
# l = [1, 2, 3] => this data cannot be converted to dictionary.
e = dict(l)

print(l)
