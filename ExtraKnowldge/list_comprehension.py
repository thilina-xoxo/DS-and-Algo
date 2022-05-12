# input multiple values in python
x,y = input().split()

# convert these two values into integers
x,y = [int(x) for x in [x,y]]

# input two values and type cast them to intergers with list comprehension
x,y = [int(x) for x in input().split()]

