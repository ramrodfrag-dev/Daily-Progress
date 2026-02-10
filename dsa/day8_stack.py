# Implementation of the stack using custom control.

class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self,x):
        self.items.append(x)
        
    def is_empty(self):
        return len(self.items)==0
        
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def show(self):
        if len(self.items)==0:
            print("NO Elements are present in the stack for showing")
            return
        for i in range(len(self.items)-1,-1,-1):
            print("|",self.items[i],"|\n-----")            
    
    
    
obj=Stack()

print(obj.is_empty())

obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
obj.push(4)
obj.push(5)

obj.show()

#
#
#
#
#
#
#


# Starting of Important concept in the stack that is monotonic stack

'''Monotomic Stack:'''
#It is a type of stack in which it keeps it's elements in a specific order may be in always increasing order or always decreasing order.
# 1.In monotonically Increasing stack: Each new element you push in to stack is greater than the ones which are already present in the stack
# Problems solved with this is: Next smaller element or previous smaller element.
# 2.In monotonically Decreasing stack: Each new element you push in to stack is less than the ones which are already present in the stack.
# Problems solved with this is: Next Larger element or previous Larger element.


'''Execution of this monotonic stack'''
#Let's take the monotoniccally decreasing stack which is used for finding next greater element.

#Step:1-> Iterate through the required list or array by creating a stack(list) and initializing it with all -1's
nums=[1,2,4,3,5,0]
results=[-1] * len(nums)
stack=[]

#Step-2-> Push if the stack is empty and if we get a greater number than top of stack then pop all elements until top of stack > current element and push this current element
# Store these values in a different list to know which element is greater than this current element.

for i,num in enumerate(nums):
    if len(stack)==0:
        stack.append(i)
    else:
        while num>stack[-1]:
            results[stack[-1]]=num
            stack.pop()
        stack.append(i)
        
        
print(results)

'''Note: Always remember store the indices in the monotonic stack not the actual numbers as we need to update the results array of many elements in 1 iteration if greatest element
is found now and all elements in the stack are lower than this element then all results indices must change so, it will be difficutlt to find the index of that number and then update it.
'''

#
#
#
#
#
#
#



'''Topic: Min,max element in the stack at a particular given time'''  #Finding the minimum and maximum of the elements of the stack at a particular given time.
# SO, after pop some elements can be gone we cannot keep the track of the min and max by a single variable.

'''Method we use: Use minstack or maxstack''' #->ex with minstack
# So, apart from the stack we have taken we should also take a minstack in which we store the elements which is the max or min of that paticular layer.
# Ex: If we have a stack=[] take min stack also minstack=[]

#If 9 comes push 9 in both minstack and stack.

#then 10 comes so, min(10,minstack[-1]) is 9 so, again 9 is pushed to min stack

# then 7 comes so, min(7,minstack[-1]) is 7 so, 7 is pushed to minstack

# so, like wise in each layer we would know until this layer which is smaller if the elements above is deleted also.

