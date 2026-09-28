# This Contains some important concepts of the OOPs things in python

''' What is class?'''
# It defines a structure and behaviour of the objects it has.
# Object has state and behaviour: state is data and behaviour is the functions which are applied on the data.

# We can create multiple new objects with the same structure we have(class)

# Objects encapsulate state and provide behavior that operates on that state.       -This is what objects do

''' 
OOPS provides modularity
We can work on seperate module without knowing the functionalities of the others. so like this we can manage them easily.
OOP becomes particularly useful when the system has many interacting entities and substantial state.

'''


'''What is OOPS:'''
#-> It is a type of programming which organizes code using objects that combine fucntions and data.
# It groups data and functions together inside a single unit called object, so that functions can directly operate on the given data->Encapsulation

''' 
Differnce between traditional and procedural Approach:
1. Traditional everything in a monolithic way all codeor users everything is in same code so, maintance and debugging is so difficult but where as the
2. Procedural everything will be in a systematic way where every user will be in a seperate file and code and methods are correctly packed and placed in files, so maintanance is easy.
'''

''' Difference between Object based approach and Object-oriented Approach'''
#-> Object based approach is nothing but it consists of objects and we can use their functions like encapsulation and other things but not the custom polymorphism, Inheritance
# where as
#-> Object oriented Approach is where along with dealing with objects we also include all the methods which consists of all the methods including with it like polymorphism, Inheritance,etc.

'''Some main concepts in OOPS are(4 common pillars in OOPS):'''
# 1.Inheritance     ->reuse behaviour of the parent class
# 2.Encapsulation   ->(restricting the direct access) Wrapping data and methods together and restricting the direct access to the internal details.
# 3.Polymoriphism   ->same interface but different behaviour (or) same function name but different functionalities in same code.
# 4.Abstraction     ->hiding complexity ->It's like what it provides instead of what internally happens.
# Note: See the difference between Encapsulation and the Abstraction
# In Encapsulation only the public methods are allowed to interact with the internal state of the objects

'''Constructor:'''
# It always runs when the object is created

class Animal:
    def __init__(self,name):
        self.name=name

a=Animal("Tinku")       # internally it calls-> Animal.__init__(a,"Tinku")
print(a.name)

# Note: Remember if the self is not written then the object does not remember its value only the constructor remembers as a variable and if again it is called then the variable is replaced the old object data is vanished.
# So, always use self while creating a class and creating objects.

#
#
#
#

''' 13-03-2026 '''

'''
Question: Writing a class name SystemLog
Requirements:
a.Constructor receives log list.
b.Method getLastLogs(minutes) returns logs from last N minutes.
c.Overload (+) operator to merge two log systems. -> It means we already has add method so, for that do a operator overload which is redefining with different parameters
Think about:
a.storing timestamps
b.filtering logs
c.operator overloading
'''

# Solution uses the operator overloading
import time
from datetime import datetime, UTC
class SystemLog:
    def __init__(self,loglist):
        self.loglist=loglist    #This loglist must contain [("message",timestamp),("message",timestamp),....]
        
    def getLastLogs(self,minutes):
        limit=minutes*60
        currenttime=time.time()
        res=[logs for logs in self.loglist
             if currenttime-logs[1]<=limit]
        return res
    
    def __add__(self,other):
        loglist=self.loglist + other.loglist       # This is called when the + operator is called as it is overloaded
        return SystemLog(loglist)
    

logs1=[("Server Down",time.time()-30),
       ("DataBase Error",time.time()-120)]      # There -30 is done in order to move 30 sec ago like to make it a older one as this all executes at once
logs2=[("Application Bug",time.time()-90),
       ("Internet Issue",time.time()-2400)]

log1=SystemLog(logs1)
log2=SystemLog(logs2)

merged=log1+log2

print(log1.getLastLogs(2.1))
print(merged.getLastLogs(1))
print(datetime.now(UTC))

#
#
#
#

#   14-03-2026

# polymorphism example:
class Cat:
    def speak(self):
        print("meow")
    
class Dog:
    def speak(self):
        print("Bark")
        
animals=[Dog(),Cat()]

for a in animals:
    a.speak()
    
#Note: Here see the method name is same but the operations they are performing are different.
# Polymorphism are of 2 types:
#1. Runtime Polymorphism(Late Binding/Dynamic Binding) ->Method Overriding and duck typing
#2. Compiler time Polymorphism(Early Binding/Static Binding) ->Method overloading ->Not available in Python

'''
Method Overriding: There is one parent and one child which extends from parent which has same method names but different functionalities.
There has to be a inheritence relationship between 2 classes(Classical subtype problem) or else ducktyping is also comes under this.

Method Overloading: Within the same class if 2 methods have same name but different functionalities or change in parameters.
They must be there in same class

Duck typing is nothing but if there is a method associated with the class whose object is being called now then it executes it.
Here if there are 2 methods in 2 different classes and an object is created on both objects and called the same function then the sunctionalities are changed.
'''


#OOPS Question:
'''
Design class:
ProcessScheduler

Requirements:
1️⃣ Constructor receives process list.
2️⃣ Each process has:
name
interval
offset

Example:
A → every interval
B → only even intervals
C → after A runs 4 times
D → only prime intervals

Write function:
getNextExecution(time)
Return which process runs at that time.
'''

# Solution:

class ProcessScheduler:
    def __init__(self,processList):
        self.processList=processList
        

processList=[("A",)]





'''Encapsulation'''

# Restaurant r = new Restaurant();
# Here the first restaurent is the datatype and the r is refernece and the new Restaurent is the object cretion thing.

# So, class allows restricted acess to the others which decide the state. Hence it has some 4 acess levels for providing the acess of its elements to others.
''' These are for fucntions which update state. direct state can be changed only within the class but its also not recommended when there are strict validation checks.

| Modifier | Same class | Same package | Subclass in different package | Everywhere |
|---|---:|---:|---:|---:|
| `private` | ✅ | ❌ | ❌ | ❌ |
| default   | ✅ | ✅ | ❌* | ❌ |
| `protected` | ✅ | ✅ | ✅** | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |
'''

# Encapsulation is not "private + getter/setter."
# It's about controlling how state is accessed and modified.


'''Specifiers vs Modifiers'''
# Specifiers tells extra info about the variables we are using and how much memory we need to keep hold for it and so on.
# Types: 
# 1.type specifiers: int, char, long, short,etc
# 2.storage specifiers: auto, register, extern, static, mutable -> these are only present in C/C++ only where we should manage memory

#a. Auto: These data is stored in stack and they gets deleted after its scope/block is done exceuting. Default it is auto. It is intialized by some garbage value instead of like 0 in case of global variables
#b. Extern: This is just declaration only and not the memory intialization as we use this when we want to acess some vaiables which are already present but we do not know where.
# -> just find it and take  reference and then we can use them. ->Understand differnce between defining and declaring
# Ex:   extern int a;
#c. Register: This puts the variable in the register memory. So, acess time is very less for us. After we put register keyword also it is compilers wish whether to keep the variable in register or not.
#d. Static: If we place this infront of a variable then that variable is shared between all the objects created by that class instead of creating one varibale per object.
# Note: For static variables or methods no object creation is required.
'''
Static methods are called as class-level methods and non static are called instance-level methods.
Note: Static Methods cannot acess non-static methods while non-static methods can acess static methods. and static does not have this keyword as it is common across all objects'''

# Modifiers are for mentioning the acess of certain things to others.
# Acess modifiers: private,default,protected,public.



''' Use of (this) key word.'''

# This is used when we want to mention it is specifically related to this object or this scope object. Ex:

class hello:
    def greet(self):    #type:ignore
        return "User"
    
    def greet(self,name):
        self.name=name
        return self.name
obj=hello().greet("anjan")

# See how the self works just like that that is in java.

''' Python does not provide method overloading as it is compiletime like Java but it implements them by using the *args and **kwargs,etc. 
Python only does method overriding by inheritance or by using the Ducktyping Principal'''
# If we try to keep the same name for 2nd method then the 2nd method replaces first one

class Parents:
    def __init__(self):
        self.value = 5
        
''' Constructor ->See above __init__'''
# It does not have return types, invoke during the object creation, cannot be inherited.
# If the child does not have a constructor then it executes the parent, else if it has then child constructor only runs
# If we want to specifically call parents constructor then use super key word
# In python constructor overloading is not there but in other languages it is there.

class Parent:
    def __init__(self):
        print("1. Parent Constructor")

class Child(Parent): # see how it is inheriting without keywords like extends in java.
    def __init__(self):
        super().__init__()  # Runs Parent constructor first
        print("2. Child Constructor")

c = Child()



'''Constructor Chaining:'''
# in java:
# class Order {

#     int id;
#     double amount;

#     Order() {
#         this(0, 0);
#     }

#     Order(int id, double amount) {
#         this.id = id;
#         this.amount = amount;
#     }
# }

# In python: the constructor over riding is only the constructor chaining as the over loading is not available.


'''final Keyword:'''
# If we put this keyword to:
#a. Variable then it cannot be reassigned but it can be changed.
#b. Method then it cannot be over ridden with child sub classes
#c. Class then it cannot be extended to its child classes.
# Final means this intialization is final and only you can make changes in this but not reassign it to other things.




'''Inheritance:'''

#Types: (Note here A is parent of all see arrow direction)
# 1. Single Inheritance A->B
# 2. Multilevel Inheritance A->B->C
# 3. Hierarchial Inheritance A->B and A->C
# 4. Multi Inheritance A->B A->C and B,C->D(Diamond Problem) Here one class can get inheritance from many classes

# See the Diamond problem is where we need to find out which methods to take from two of classes it inherited if the fucntions are over riding.
# see it like a diamond

# Java does not allow multi inheritance so there will be no problem but python accepts so it solves by MRO(Method Resolution Order)
# So, it has a order which tells like first there is a class and then next and so on and we could get an idea of from where we need to inherit a particular method.
# Ex: MRO= D->B->C->A   in the previous examples. so if the method is found in d fine otherwise goto B and so on.
class D:
    pass
print(D.mro())


# Problems with inheritance:
# a. Tight Coupling: One component can affect other.
# b. Deep Inheritance Trees. so if 1 part in root level breaks then all tree need to be updated again.
# c. Reduced flexibility: Inheritance makes us follow a hirarchy which is not good

# What should we follow:
#Soln: 
# a. Composition which is not a hierarchial process. It is just building class by using objects of other classes.
# b. Composition: has-a relationship whereas inheritance: is-a relationship
# c. It has loose Coupling.


'''Note: When a child calls a parent method then also no parent object is created, always only child object is created and it may use parent methods and variables'''





# 27-09-2026

res=isinstance(payment,CardPayment) #type:ignore
#-> Here payment is a other new object. If this object is an instance of CardPayment then it returns True else False

# ->Polymorphism which does not contain Inheritance are loosely coupled, cleaner code, easy maintainability,etc

'''Dynamic Dispatch(C++,Java) totally works with the Hierarchial System and the Ducktyping(Python,go) totally works on the Existing of the methods in the code'''


def add(self, *args):
    return sum(args)    # Like this python makes the compiler time po;ymorphism. so if the 2 arguments add comes or 3 comes then always it gives correct solution.

# ->In java Overoading happens if we change the no.of parameters or their return types but no with their return type as it still be ambiguous


'''In java Dynamic Dispatch we generally take the created objects methods only and no the references methods '''
# Ex:
class UPIPayments():
    def pay(self):
        pass
    pass
# Payment p = new UPIPayment()  ->Eventhough the reference is Project but the real object created is simple so its methods are used. This is done by Dynamic Method Dispatch

# Note: Python does have the Static reference thing only it just stores in a variable without any data type. So, it always checks objects methods and executes them, no issue.
p= UPIPayments()
p.pay()


'''What things cannot be overridden in the objects:
1. final keyword methods: These cannot be fixed once initialized
2. static keyword methods: These are not visible only
3. Constructors: These are not inherited by the child. so it cannot be overridden
4.Private methods: These are not accessible to child as an inherited methods, so they cannot
'''

'''override Method'''
# This is not at all for the runtime. It is just for the compiler time error finding. While compiling if we write any method in child which we want to override name inccorectly
# Then it does not throw any error and directly executes the parents class. In order to prevent this we use @override to make compiler understand we are overriding a function which already exists.
# If the name is incorrect then it say you are not overriding and method and raises error which we can check and solve later.


# Encapsulation: Control acess to data/implementation while the Abstraction: Hides unnecessary Implementation Complexity.

'''Abstract Method'''
#Ex:
from abc import ABC, abstractmethod
class Payment(ABC):

    def validate(self):
        print("Common validation")  #This method is shared across all subclasses of it and they do not need to compulsorily define this method. ->See this is concrete method in abstarct class

    @abstractmethod
    def pay(self, amount):          # Ensures all subclasses must have this method or behaviour with them as this is not shared to them
        pass
    
class UPIPayment(Payment):

    def pay(self, amount):
        print("Pay using UPI")


class CardPayment(Payment):

    def pay(self, amount):
        print("Pay using card")
        
# Payment()        # ❌ cannot instantiate  #Remove comment and check
UPIPayment()     # ✅

#Definition:
# 1.Abstract Methods:It is a method that is declared, but contains no implementation (no body). It acts as a contract or requirement for child classes(Concrete classes).
# 2.Abstract class:It is a base class that cannot be instantiated directly (you cannot create an object using new AbstractClass() or AbstractClass()). It exists solely to serve as a common parent blueprint for other classes.

# ->If we put the abstract method to a method then the class also becomes abstract
# ->If a concrete classs does not declare the things that the abstarct class said then this class also becomes abstarct.
# ->Abstract classes cannot be instantiated and results in error.
# ->Abstarct classes enforces a Uniform Interface: It ensures all child classes implement a standardized set of behaviors while sharing common functionality.
# ->Abstarct class can have concrete methods
# Ex: Vechile is very abstarct to include methods like horn or engine performance, or fuel capacity, So it acts like a abstarct class to enforce all concrete classes under it to have all these variables and methods(Car,bike)


# Abstract class → "What kind of thing are you?"
# Interface      → "What can you do?"           See in word file

# Ex:
# Vehicle
#   └── abstract class

# Flyable
#   └── interface/capability

# Bird
#   ├── is a Vehicle? maybe not
#   └── can Fly



# UML(Unified modeling language): How we can represent relations between objects or others

# 1. Association: Two Independent objects which can sustain independently have a relation(IS-A) are related.
# 2. Aggregation: Two objects(Parent and child) which have relation(HAS-A weak ownership) and can exists independently are related.
# 3. Composition: Two objects(Parent and child) which have relation(HAS-A strong ownership) and cannot exists independently are related.
# See all 3 details in the word file.

# Understand:
#                 OOP
#                  │
#      ┌───────────┼────────────┐
#      ▼           ▼            ▼
# Encapsulation Abstraction Inheritance
#      │           │            │
#      └───────────┴────────────┘
#                  │
#                  ▼
#             Polymorphism



'''Exception Handling: It is something which we use to handle an error instead of making it crash.'''

# Without Exceptional handling our Program will terminate suddenly, if we handle it then it can be recovered and continued
# Use these only where there is a potential risk of getting an error.

#
#       Throwable (Root)
#          /       \
#   Error           Exception
#                  /         \
#   Unchecked (Runtime)     Checked (Compile-Time)
#

# Checked vs UnChecked Exceptions (Only java)
# Checked: These are the exceptions which the compiler excepts to solve beforehand running Ex: IOException, SQLException
# UnChecked: These are exceptions which the compiler ignore in the beginning Ex: ArithmaticException, NullPointerException

# Note: Python does not have such kind of exceptions

''' Common terms:'''
#1.(try,except,finally)Ex:
x=0
try:                                        # This will initially run.
    result = 10 / x
except ValueError:                          # If there is ValueError in the try block then this is excepted here.
    print("Value must be positive")
except ZeroDivisionError:                   # If there is ZeroDivisionError then it excepted here in this except block
    print("Cannot divide by zero")
except Exception as e:                      # If there is any other error other than we excepted then it come here and we can handle it here
    print(f"An unexpected error occurred: {e}")
else:                                       # If it runs sucessfully then it executes this thing
    print("Successful")
finally:                                    # This runs regardless of what happens in the try and except blocks
    print("Cleanup")


#2.(raise)How to raise/propagate a Error:
amount=10
if amount <= 0:
    raise ValueError("Amount must be positive")


#3.(Custome Exception Handling) There are custom generated Exception handlings also:
class InsufficientBalanceError(Exception):
    pass
balance=20
if  amount > balance:
    raise InsufficientBalanceError()



# throw new ValueError ->in java just like raise
#void readFile() throws IOException { } -> this says we can expect a error from this function   -> this equivalent is not there in python


'''Exception Hierarchy'''
#BaseException
    # │
    # └── Exception
    #       ├── ValueError
    #       ├── TypeError
    #       ├── KeyError
    #       ├── IndexError
    #       └── ...
    

'''Differnce between raising and the handling(When to use what)'''
#Raising is used when a function detects an invalid state and needs to trigger an error signal (raise),
# while handling is used by the calling code (try-except) to catch that signal and recover so the program doesn't crash.
# In a good program both will be there and if there is any user mistakes or small mistakes then an error is raised otherwise they need to be handled by the system.

# EXCEPTIONS
# try       → risky code
# except    → handle
# else      → no exception
# finally   → cleanup
# raise     → explicitly raise
# custom    → domain-specific errors

# JAVA:
# checked   → compiler-enforced handling/declaration
# unchecked → RuntimeException hierarchy
# throw     → throw exception
# throws    → declare possible exception