# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(num1, num2):
    return num1 + num2

# print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):
    result = 0
    for x in a:
        result += x
    return result

#print(f2(1))                    # Should print 1
#print(f2(1, 3))                 # Should print 4
#print(f2(1, 4, -12))            # Should print -7
#print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

# a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
def f2(a):
    result = 0
    for x in a:
        result += x
    return result

# print(f2(a))    # Should print 22
# change *args --> a and uncomment the a list

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(num1, num2=1):
    return num1 + num2

#print(f3(1, 2))  # Should print 3
#print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**vals):
    # print("key: a, value: " + str(vals["a"]))
    # print("key: b, value: " + str(vals["b"]))
    ### loop through and print each value 
    ### review the .items() --> dictionaries .items(), .keys(), 1 more
    for args, items in vals.items():
        print(args, items)


# Should print
# key: a, value: 12
# key: b, value: 30
# f4(a=12, b=30)

### not need, f4 on 63 - 69 works for both 
# def f4(**vals):
#     print("key: city, value: " + vals["city"])
#     print("key: population, value: " +str(vals["population"]))
#     print("key: founded, value: " +vals["founded"])

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
# f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# works, but doesn't use **kwargs
# def f4(d):
#     print(d)

def f4(**vals):
    print(vals["d"])

# How do you have to modify the f4 call below to make this work?
# f4(d = {  "monster": "goblin", "hp": 3})


# example from lecture Tuesday, July 7th
# def stupid_add(a, b):
#     if type(a) == str and type(b) == str:
#         print(int(a) + int(b))
#     elif type(a) == int and type(b) == int:
#         print(str(a) + str(b))
#     else:
#         print(None)


# stupid_add("1", "2")
# stupid_add(1, 2)
# stupid_add(1, "2")
