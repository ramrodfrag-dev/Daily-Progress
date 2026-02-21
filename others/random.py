
# def subarraySum(nums: list[int], k: int):
#     left=0
#     right=0
#     hashe={}
#     sum=0
#     count=0
    
#     for i,num in enumerate(nums):
#         sum+=num
#         if sum==k:
#             count+=1
            
#         if sum-k in hashe:
#             j=hashe.get(sum-k)
#             count+=j
        
#         if sum not in hashe:
#             hashe.update({sum:1})
#         else:
#             j=hashe.get(sum)
#             hashe.update({sum:j+1})
    
#     print(count)
    
# nums=[0,0,0,0,0,0,0,0,0,0]
# k=0

# subarraySum(nums,k)



#
#
#
#
#        
        
# Next Greatest Element        

# nums=[1,2,4,3,5,0,1]
# results=[-1] * len(nums)
# stack=[]

# #Step-2-> Push if the stack is empty and if we get a greater number than top of stack then pop all elements until top of stack > current element and push this current element

# for i,num in enumerate(nums):
#     if len(stack)==0:
#         stack.append(i)
#     else:
#         while num>nums[stack[-1]]:
#             results[stack[-1]]=num
#             stack.pop()
#             if len(stack)==0: break
#         stack.append(i)
        
        
# print(results)

#
#
#
#
#

#Binary Tree Level Order Traversal
import collections

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left
        
    def __repr__(self):                         #To make python understand how our custom class can be accessed.
        return f"{self.val}"
        
root=TreeNode()
root.val=45
que=collections.deque([root])

print(que)
