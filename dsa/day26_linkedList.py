
# 19-08-2026 (Day 26)

"Reorder Linked"

# LeetCode: ->143
# We are given with a linked list and we need to reorder in a certain way
#Ex: input=[0, 1, 2, 3, 4, 5, 6], output=[0, 6, 1, 5, 2, 4, 3], general rearrangement is [0, n-1, 1, n-2, 2, n-3, ...]
###Soln:
# Here if we closely observe last half elements are coming to the front in between 
# and if we observe second half of linked list is being revered and then they are array to the first half alternatively.
# Remember to just make the first half last node points to null and then make pointers move correctly instead of getting something like None.next in the code.
# Store necessary pointers and intialize required and update carefully.

#
#
#
#
#

# 19-08-2026 (Day 27)

"Shallow and deep copy Info"
# For details completely see: dsa\python_core_practice.py in main folder.
# Ex:
# head
#  ↓
# 1 → 2 → 3 → None

"Shallow copy"
# If we apply for the linked list then it will be:

head=ListNode() # type:ignore
import copy
head2 = copy.copy(head)

# head  ──► Node(1) ───────► Node(2) ───► Node(3)

# head2 ──► Node(1) ────────┘

# so, only the first node will be copied and others will be pointing to the same things.

"Deep copy"
# Original:
# head
#  ↓
# 1 → 2 → 3


# Deep copy:
# head2
#  ↓
# 1 → 2 → 3

# so,m every thing will be seperate and can be used seperated.
# for making deep cody first make each node and put the values required and then move to the next node.

#
#
#
#
#

