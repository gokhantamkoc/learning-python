# Syntax of a lambda function
# lambda arguments: expression

# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

# the same behavior with function definition


def double(x):
    return x * 2


print(double(5))

# use filter with lambda expression

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

filtered_list = list(filter(lambda x: (x % 2 == 0), my_list))

# Output: [4, 6, 8, 12]
print(filtered_list)

# use map with lambda expression

mapped_list = list(map(lambda x: x * 2, my_list))

print(mapped_list)
