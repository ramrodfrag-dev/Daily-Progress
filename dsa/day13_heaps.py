# It contains everything related to the Heaps and its some important questions

'''
Heap: It is a binary tree structure.
->It has 2 types of heaps:
a. min-heap-> It's parents value is less than children value
b. max-heap-> It's parents value is grater than children value

'''

# some points are(w.r.t array implementation of min heap):
# 1. Worst Time complexity of Insertion and deletion is O(logn)
# 2. Worst Time complexity of Searching something largest element or any other element except the min element of whole heap it takes O(n)
# 3. For finding the least element in the heap it takes O(1 as the first element is the min element)
# 4. Building the entire heap by using .heappush takes O(nlogn) whereas it takes O(n) by using the .heapify
# Reason for the 4th one is here while adding all nodes at once we only update the non-leaf nodes which are less than total no.of nodes and takes less time like O(n)


'''Implementation'''
# In python we can generally implement only the min heap. SO, to implement maxheap we will keep the -ve sign to the numbers and do the min heap and finally convert to the +ve values

import heapq

heap=[]

heapq.heappush(heap,23)
# heapq.heappush(heap,(2,"Sending Hello"))       -> If we want to store any tuples also we can do. But other structures like dictionaries,sets are not allowed

heapq.heappush(heap,65)

print(heap)

print(heapq.heappop(heap))

print(heap)

# for directly converting the whole list to the heap then just use the function heapify
li=[3,5,23,6,1,89,34,23]

heapq.heapify(li)

print(li)

# -> For max heap we can use the -ve numbers or use the function heapq._heapify_max which makes the maxheap

heapq._heapify_max(li)

print(li)

#-> To find the nth smallest or nth largest element in a heap we use the below functions:

n=3
small=heapq.nsmallest(n,li)[-1]
large=heapq.nlargest(n,li)[-1]

print(f"{n}th smallest number is {small} and the {n}th largest number is {large}")


'''Heap is used for finding kth largest or smallest number instead of sorting because sorting takes O(nlogn) generally and the heap takes O(nlogk) k is the depth of the tree unlike n which is all elements'''
#
#
#
#
#

''' Solving the Scheduling thing by using the heap'''
# Steps required:
# 1. Use tuples and store the both the (available_next_slot, capacity)  -> remember always the heap only aranges and heapifies with the first number in the tuples provided so, it must be priority or something which is available now.
# 2. Remove the top one which can be available now only(it heapifies internally) and assign work and update the next_available slot and push it back to heap and it heapifies it

'''Question:
Problem 3 (Logic Builder — Custom Problem)

Two animals are managing a forest food distribution system.
Each animal has a food capacity:
animals = [5,7,3]

Food packages require loads:
food = [2,4,6,1,3,5]

Rules:
An animal can carry food if capacity ≥ food weight
Carrying takes 1 minute
After carrying, the animal rests 1 minute
Animals work in parallel
Return minimum time to move all food or -1.

Constraints:
1 ≤ animals ≤ 10^5
1 ≤ food ≤ 10^5

Hint:
Earliest available worker → min heap

Try to think about:
(next available time, capacity)
'''

# Solution:

animals = [5,7,3]
food = [2,4,6,1,3,5]

heap.clear()

animals.sort()  # animals = [3,5,7]
food.sort()     # food = [1,2,3,4,5,6]
def mintime(animals,food):
    if animals[-1]<food[-1]:
        return -1

    animals=[(0,a) for a in animals]
    heapq.heapify(animals)
    time=0
    
    for item in food:
        while True:
            slot,cap=heapq.heappop(animals)
            if cap>=item:
                time=max(time,slot+1)
                heapq.heappush(animals,(slot+2,cap))
                break
                
    return time

time=mintime(animals,food)
print(f"Minimum time required={time}")


animals2= [150,152,148,160,155,149,151,153,154,158,
           157,159,156,161,162,163,164,165,166,167]
food2 =[x for x in range(1,101,1)]

print(f"Minimum time required={mintime(animals2,food2)}")
