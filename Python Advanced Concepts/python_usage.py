# It contains some advance functions to use:

''' In Recursions and BackTracking do not reintialize variables in the inner loops.'''

#Ex:

x=10
def func():
    x+=1    #type:ignore
    print(x)
    
print(x)

#Remove the type ignore and see the difference.

# Whenever we are trying to update a variable which is already intialized outside the function then it accepts it.
# But when we are trying to reinitialize the variable then the error appears as we cannot do it.

###Soln:
# Place a nonlocal keyword or the global keyword to access the variables and let then reintialize.

y=10
def func2():
    global y
    y+=1
    print(x)

print(y)
# Here both executes.

# global is used when we need to acess the variables which are not in any parent outer loops.
# nonlocal is used to acess the variables which is in parent outer loops.



'''How to use the class keyword'''

# When we want to initialize a class we will use the class keyword and some constructor and also some methods and variables in it.
# Ex:

class anjan:
    def __init__(self):
        st={}
        op=True

# When we want to inherit from other classes then we use the () and put the parent class name inside the brackets
# Ex:

class hero(anjan):
    def __init__(self):
        super().__init__
        print("hello")
        
        