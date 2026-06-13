
# Day 15:

'''
Decorators:
-> A python Decorator is a function which takes other function as an argument and adds some additional functionality to that function and returns a new function without modifying the original code(function)
(or) A decorator wraps a function and modifies its behavior without changing its code.
These are higher order functions often used for tasks like the logging, Authentication, and caching,etc
'''

#Ex:

def special_div(func):      #This is the decorator
    def wrapper(a,b):       #Function to replace the original function with
        if a<b:
            a,b=b,a
        func(a,b)
    return wrapper

@special_div
def div(a,b):               #This is original function
    print(a/b)

# div=special_div(div)      This is just used if we remove the @decorator name to the original function(It's just what internally does).

div(3,6)