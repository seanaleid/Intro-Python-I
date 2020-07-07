# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables
# found solution at https://www.programiz.com/python-programming/global-keyword using the global keyword inside the function

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
# print(x)


# This nested function has a similar problem.

### VERSION 2
### Found teh solution at https://www.programiz.com/python-programming/global-local-nonlocal-variables under Nonlocal Variables
### had to use nonlocal instead of global
def outer():
    y = 120

    def inner():
        nonlocal y 
        y = 999
        print("This is y inside the inner() function", y)

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print("This is y inside the outer() function", y)

outer()
# print("This is y outside of everything", y)



### VERSION 1
# def outer():
#     y = 120

#     def inner():
#         global y 
#         y = 999
#         print("This is y inside the inner() function", y)

    # return inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    # print("This is y inside the outer() function", y)

# outer()
# print("This is y outside of everything", y)
