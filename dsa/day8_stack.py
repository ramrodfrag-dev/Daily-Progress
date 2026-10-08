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
        while stack and num>stack[-1]:
            results[stack[-1]]=num
            stack.pop()
        stack.append(i)
        
# The above code is for monotoically Decreasing stack    
print(results)

'''Note: Always remember store the indices in the monotonic stack not the actual numbers as we need to update the results array of many elements in 1 iteration if greatest element
is found now and all elements in the stack are lower than this element then all results indices must change so, it will be difficutlt to find the index of that number and then update it.
'''

# -> Even we can store a mixed number of types in single list in one cell in stack and use them as per the question is concerened with
# ->Ex:LeetCode 739 :It tells to give a output array in which for each element after how many places its greater number is availale, if not available then we return 0.

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


# 6-10-26 (DSA Day 37)

'''Max score of the parantheses'''
# Leetcode:856  ->Here we are given with a string which is valid for sure and we have to find it score
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

## Intuition: Here we will use stack as they are paranthesis and then First we think adding the paranthesis in it and if we get calculate whent there is right paranthesis but how to keep track how many inner brackets are there in each and in the A+B format or AB format?
# So, we are here storing the values in the stack so that at each level we can checkare there any inner subbrackets before if yes multiply the score with 2 and if not leave it and at last add all those things to get result

def scoreOfParentheses(self, s: str) -> int:
    stack=[]
    score=0

    for i in s:
        if i=='(':
            stack.append(-1)
        else:
            score=0
            while stack[-1]!=-1:
                score+=stack.pop()      # Here add all scores until -1 comes as we are getting all the inner brakets a,b scores(()())
            
            if score==0:
                stack[-1]=1
            else:
                stack[-1]=2*score       # if the score!=-1 then there are some inner brackets and we multiply those score with 2 and put in the stack
    
    return sum(stack)       # Here we are summing because there are left overs like ()() so we need to combine them and give result




# 7-10-2026 (DSA Day 38)

'''Longest Valid paranthesis'''
# Leetcode 5:

s=")()())()()(" # SO what is the longest valid palindrome of the string which is 4 here.

###Intuition:
# ->First for '(' bracket put this directly into the stack
# ->If we encounter ')' then we will check whether we have numbers below if yes add all those until we find end of array or other character then if the character is '(' then add 2 to the score and pop the '(' and then check if there are any more numbers below the '(' and if yes add them and finally append score.
# ->If the we did not encounter '(' then we will reappend the score we have taken and then append the closing bracket finally

#                                  Char in String
#                                       │
#                    ┌──────────────────┴──────────────────┐
#                    │                                     │
#              char == '('                           char == ')'
#                    │                                     │
#                    ▼                                     ▼
#              stack.append('(')                      score = 0
#                    │                                     │
#                    │                          ┌──────────┴──────────┐
#                    │                          │ Pop & sum pre-ints: │
#                    │                          │ score += stack.pop()│
#                    │                          └──────────┬──────────┘
#                    │                                     │
#                    │                           ┌─────────┴─────────┐
#                    │                           │ stack[-1] == '('? │
#                    │                           └────┬──────────┬────┘
#                    │                             Yes│        No│
#                    │                                ▼          ▼
#                    │                           MATCH!     UNMATCHED!
#                    │                         1. score+=2  1. if score>0:
#                    │                         2. stack.pop()    append(score)
#                    │                         3. Pop/add   2. append(')')
#                    │                            prev-ints
#                    │                         4. append(score)
#                    │                                │          │
#                    └────────────────────────┬───────┴──────────┘
#                                             │
#                                             ▼
#                                   Loop end: max(ints in stack)




# 8-10-2026 (DSA Day 39)

'''Longest Palindrome substring: Leetcode(5)'''
# Here we are given with a string and we have to tell which is the longest palindrome in it.
## Intuition: Always remember when there are paranthesis think of stacks and when there are Palindrome think of taking 2 pointer and traversing 1 from front and 1 from back.
# But if we do 1 from front and 1 from back in this question then the over all complexity will become n^2 * n as n is for checking palindrome and the n^2 is for the selection of all palindrome of all lengths in the worst case complexity.

# So, there's other way to think when asking about palindrom and (longest or no.of palindromes or ways) are asked:
# => We will traverse the given string adn at each character we will expand towards the both sides by pointers and check whether the given string is a palindrome or not.

longest,start,end=0,0,0
def max_palin(l,r):
    global longest,start,end
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>longest:
            longest,start,end=r-l+1,l,r
        l-=1
        r+=1

for i in range(len(s)):
    # For odd cases:
    max_palin(i,i)
    # For even cases:
    max_palin(i,i+1)

'''This is one of most important pattern of expanding the palindrome and checking instead of always reducing the string from both sides and checking it'''