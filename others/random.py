
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
        
nums=[1,2,4,3,5,0,1]
results=[-1] * len(nums)
stack=[]

#Step-2-> Push if the stack is empty and if we get a greater number than top of stack then pop all elements until top of stack > current element and push this current element

for i,num in enumerate(nums):
    if len(stack)==0:
        stack.append(i)
    else:
        while num>nums[stack[-1]]:
            results[stack[-1]]=num
            stack.pop()
            if len(stack)==0: break
        stack.append(i)
        
        
print(results)


