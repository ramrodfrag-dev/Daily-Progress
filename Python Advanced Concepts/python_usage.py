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


'''Some facts:'''
a=9000000
b=9000000
mid=(a+b)//2
# The above thing works in python as the integer holding capacity is way more and they are expandable unlike other languages like c++ or java where they may overflow and can cause many unwanted results
# So, instead of doing the above method we use as below:
mid=a+((b-a)//2)    #-> With this we can make sure they never cross the limit/capcity to hold.

