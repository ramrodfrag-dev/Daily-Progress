# This Contains some important concepts of the OOPs things in python

'''What is OOPS:'''
#->It is a tpe of programming which organizes code using objects that combine fucntions and data.
# It groups data and functions together inside a single unit called object, so that functions can directly operate on the given data->Encapsulation

'''Some main concepts in OOPS are:'''
# 1.Inheritance     ->reuse behaviour of the parent class
# 2.Encapsulation   ->(restricting the direct access) Wrapping data and methods together and restricting the direct access to the internal details.
# 3.Polymoriphism   ->same interface but different behaviour (or) same function name but different functionalities in same code.
# 4.Abstraction     ->hiding complexity
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