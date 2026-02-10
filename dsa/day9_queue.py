
# For Implementing queue with lists has more complexity as it is not feasible beacuse while popping the elements if we delete
# element at front then we need to shift all the others elements to the beginning but consider waste of time O(n) complexity

'''Instead we use the simple deque(doubly-ended queue) for all these operations'''
from collections import deque

class Queue:
    def __init__(self):
        self.q=deque()
        
    def push(self,val):
        self.q.append(val)
        
    def pop(self):
        if self.is_empty(): return
        return self.q.popleft()
    
    def front(self):
        return self.q[0]
    
    def is_empty(self):
        return len(self.q)==0
    
    

# Operations allowed for deque is:
# 1.append(val) ->appends to the right of the dequeue
# 2.appendleft(val) ->appends to the right of the dequeue
# 3. pop() ->pops the element from the right side of the dequeue
# 4. popledt() ->pops the element from the left side of the dequeue
# 5. clear() ->will clear all the dequeue
# 6. extend(li) ->It just adds all elements in li to the right of deque just like adding for loop for li to append in deque
# 7. extendleft(li) ->It adds all the elements to the deque to the left but here order changes
# 8. rotate(val) ->It rotates whole deque clockwise by val no.of times. If the val is -ve then all elements roates val no.of times anticlockwise in deque

'''
Ex: q=dequeue([1,2])
q.extend([3,4])  ->q=[1,2,3,4]
q.extendleft([5,6]) ->q=[6,5,1,2,3,4]

q.rotate(3) ->q=[2,3,4,6,5,1]

See how order changes in extendleft.It's just like using appendleft continously in a loop
'''


# -> These are the basic functionalities of the dequeue and how it shits the elements to the left of queue when a element is popped from left is:
 
#
#
#
#
#
#
#

# LeetCode: 933->Number of Recent Calls, 232->Implement Queue by 2 stacks and 102-> Binary Tree Level Order Traversal

#232: It is simple just take 2 stacks and just add normally when adding but when deleting just pop all elements from 1 stack to other and then pop 1 element and then pop all the elements from the second one to the 1st one.

#933: Here there are sending one value at a time and we need to send the count of all values present in the deque now whose difference is <=3000 including the value came now.
# First I though of counting them when they are added by using a for loop from starting or backwards but it takes lots of time
# Approach Used: Delete elements whose difference is >3000 with the current entering element before adding it. So in this way we only have values whose maximum differences is <=3000 and the length of the deque can be returned as the output.

#102: 