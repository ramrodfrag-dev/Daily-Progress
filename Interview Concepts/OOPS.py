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
#1. Runtime Polymorphism ->Method Overriding and duck typing
#2. Compiler time Polymorphism ->Method overloading

'''
Method Overriding: There is one parent and one child which extends from parent which has same method names but different functionalities.
There has to be a inheritence relationship between 2 classes

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

''' Python does not provide method overloading as it is compiletime. It only does method overriding by inheritance'''

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


