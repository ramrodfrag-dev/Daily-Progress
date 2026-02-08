# def subarraySum(nums: list[int], k: int):
#     left=0
#     right=0
#     results=[]
#     windowSum=nums[right]
#     ele=[nums[right]]

#     while(right>=left and left<len(nums) and right<len(nums)):
#         if windowSum==k:
#             results.append(ele.copy())     # copy is important as it is still connected 
#         elif windowSum>k and right>left:
#             windowSum-=ele[0]
#             ele=ele[1:]
#             left+=1
#             continue
        
#         if right<len(nums)-1:
#             right+=1
#             ele.append(nums[right])
#             windowSum+=nums[right]
#         elif right>=len(nums)-1:
#             windowSum-=ele[0]
#             ele=ele[1:]
#             left+=1
#         elif right>len(nums) and left>=len(nums):
#             break
    
#     print(results, len(results))
    
# nums=[1,9,5,0,4,2,6,3,8,1,7]
# k=9

# subarraySum(nums,k)
        
#Above thing is for the only positive thing optimal code. But for negatives we have other code:

def subarraySum(nums: list[int], k: int):
    left=0
    right=0
    hashe={}
    sum=0
    count=0
    
    for i,num in enumerate(nums):
        sum+=num
        if sum==k:
            count+=1
            
        if sum-k in hashe:
            j=hashe.get(sum-k)
            count+=j
        
        if sum not in hashe:
            hashe.update({sum:1})
        else:
            j=hashe.get(sum)
            hashe.update({sum:j+1})
    
    print(count)
    
nums=[0,0,0,0,0,0,0,0,0,0]
k=0

subarraySum(nums,k)
        