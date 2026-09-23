
# Some time instead of trying the best optimal solution trying this greedy approach will be faster and takes less memory.

''' Greedy Always tries to maximize its profit and do it greedily by selectign the best solution that is availbel now without thinking about the future consequences.'''
# For any problem always try the greedy approach. If it does it it correctly then use that only but if it gets some wrong results in some edge cases then go for optimal solution.


# 13-09-2026(Day 34)

" LeetCode 55 - Jump Game "

# Why DP is not preferable here:
# DP can solve Jump Game, but a straightforward DP solution tries
# many possible jumps from every index.
# This can take O(n^2) time, which is unnecessary and can cause TLE.
#
# Greedy is preferred because we only need to know the FARTHest index
# that can be reached so far, not every possible path.

def canJump(self, nums: list[int]) -> bool:
    goal=len(nums)-1

    for i in range(len(nums)-1,-1,-1):
        if  i+nums[i]>=goal:
            goal=i
    
    return goal==0


# In the code we move the goal from last position to the first position slowly based on nums if they can cross the goal the it is the new goal.




"Leetcode: 45 -> Jump2"

# Here we will definately reach the final point but what are the minimum no.of steps to make to the end. 

## We will take a variable farthest and make it 0. first we will insert the first element in to the queue and then we will pop it and check all the elemnts which can reach farthet and then we will add all the elements until then to the queue and continue
# Like this we will not add the repeatative elements in to queue and we will count after each level like in bfs to see the min depth where we reach the index of final element and then we return it at the end.
#
# Code

# while q:
#     farthest=0
#     n=q[0]
#     for i in range(len(q)):
#         x=q.popleft()
#         dist=x+nums[x]
#         farthest=max(dist,farthest)
#     level+=1
#     if farthest>=len(nums)-1:
#         return level
#     for i in range(n+1,min(len(nums)-1,farthest)+1):
#         q.append(i)



"Leetcode: 1696 -> Jump6"

# Here we should move to last index from the first index and at any time we cannot move more than k steps which is given. So, what will be the max amount we can get until we reach the final node. If we go to a index we will pick it up.

## Clue:
# Here we can use the dp and we should think like:
# dp[i] is the max amount we can collect until we reach i including amount at index
# We know at the last index we can get max of that amount only as we must collect it and there is nothing there after that to collect.

# and for each other index we will travel back and see the upcoming  k indexes and check which one is giving the highest value and add that to it.

# Maintain a monotonic decreasing queue where it stores all the highest amount indexes first and then the we use that to update the dp. Code looks like below:

from collections import deque
q=deque()
nums = [1,-1,-2,4,-7,3]
k=2
dp=[0]*len(nums)
dp[len(nums)-1]=nums[-1]
q.append(len(nums)-1)
for i in range(len(nums)-2,-1,-1):
    if q[0]>i+k:                    #if the last index is more than the window size then pop it out
        q.popleft()
    dp[i]=nums[i]+dp[q[0]]
    while q and dp[q[-1]]<dp[i]:    #pop all the results out of queue which are less than the current result from back
        q.pop()
    q.append(i)                     #Append at the back
    
 
    
"Leetcode: 1871 -> Jump7"

# Here a string is given and the first index is '0' we can jump to next index such that we should jump atleast minJump indexes forward or atmax maxJump indexes forward.
# If we reach end of list then return true otherwise false.

# Here take a variable farthest and store the index until which we have already cheacking previously inorder to not check once more in order to avoid tle.
# Take a queue and push all the '0''s indixes which can be achieved from the current index with help of minJump and the maxJump. if one also then also update the farthest as we have checked until then.
# If the index is len(s)-1 when appending to the queue then return True. else at the end retur False.

# Here Greedy like the jump game 1 is not working like taking a gaol and moving backwards, as we are missng some things as the steps we can take are restricted by min and max Jumps




#
#
#

# 24-09-2026 (Day 35)

"Fall Prevention (Tell Good or bad)" # ->https://www.codechef.com/problems/FALLPR

# An array is given and it is good if all the prefix sums are > 0.
# And even if some prefix sums are -ve you are allowed an operation just delete a number in a array and make all prefixes>0
# Note: only one number can be deleted

##Soln: See to make all prefixes +ve we must have -ve numbers as minimum as possible so all sums>0 if at all there is -ve we tend to make it smaller.
# Ex: if there are 2 -ve numbers then we take the big -ve number as it is destructing more to our array.

'''Steps:
1. Take a max_heap and push -ve numbers as soon as they appear and also maintain a variable remove=False and a total variable for calculation prefix sum until now.
2. Now if total becomes -ve then see whether removed is True or False.
3. IF it is True then return "NO"
4. If it is False then make it True and also popout most smallest number from heap(Biggest -ve) and then add to total. this is to give one chance and continue further.
5. make sure the total<0 and removed ==True at the end as sometimes after removed a -ve number also they will be -ve and next number will be so huge and we might not notice them.
'''

