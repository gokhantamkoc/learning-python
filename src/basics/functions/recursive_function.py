# We know that in Python, a function can call other functions.
# It is even possible for the function to call itself.
# These type of construct are termed as recursive functions.

# Following is an example of recursive function to find the factorial of an integer.
# Factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.


def calc_factorial(x):

    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)

num = 4
print("The factorial of", num, "is", calc_factorial(num))

# Recursiveness of the function can be shown like below

"""
calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
"""

# Advantages of recursion

# 1. Recursive functions make the code look clean and elegant.
# 2. A complex task can be broken down into simpler sub-problems using recursion.
# 3. Sequence generation is easier with recursion than using some nested iteration.

# Disadvantages of recursion

# 1. Sometimes the logic behind recursion is hard to follow through.
# 2. Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# 3. Recursive functions are hard to debug.

