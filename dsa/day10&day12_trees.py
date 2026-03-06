
import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This is for the Level Order Traversal for any binary or any other tree

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res=[]
        if not root:
            return res
        que=collections.deque([root])

        while que:

            level_items=[]
            for _ in range(0,len(que)):
                node=que.popleft()
                level_items.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

                # if node.children:
                #     queue.extend(node.children)       ->This is only when there are many children and they are in a array.

            res.append(level_items)

        return res
    

# For calling it first initialize root and some nodes in it

'''Process:
-> First take a results array and then queue for tracking as in the level order traversal we need BFS so we use queue.
---> Now iterate outerloop until the queue is empty and then iterate in the inner loop to the length of queue to get the each level elements
---> While iterating in the inner loop first popleft element and then add all it's children and then leave. Continue until length of queue 
then we get to know at each iteration these are the level elements.
->Finally store the level elements in the results and return it.
'''
# Think if the recursion is not possible then how could we solve it.
#
#
#
#
#



# Depth first search
'''LeetCode-112'''
# Here we are given with a target value which we need to find a path from root to the leaf node so, that its path match to this.
#I used the recursion instead of just using the stack data structure, and each time I called the recurse function I have updated the targetSum which I still require from the below branch. so that it becomes easier with less variables.

'''Balanced Binary tree'''
# It means for any node in the binary tree the differences in the heights of its left subtree and right subtree must be in <=1
# So, I have used the same recursion dfs only but this time I have returned height of subtrees in order to know the differnce.
def height(self, root: Optional[TreeNode]):
        if not root: return 0

        left=self.height(root.left)
        if left== -1: return -1
        
        right=self.height(root.right)
        if right== -1: return -1
        
        if abs(right-left)>1:
            return -1

        return max(right, left)+1


# if we see the difference is greater then we will directly return -1 to each and every layer.

'''Island problem-200'''
# here we have to see how many connected islands are there in total. all the connected islands are considered as one and others are different.
#
# We will be given a m*n matrix which contains all the islands like a grid and we would also get info about how islands can be connected like horizontally or vertically or diagonally.
#Idea:
# Think of it like a graph problem, First take a one island i.e is one node and then see what are the other nodes that are connected i.e islands. Apply any traversal and get the answer.
# Use some variables like island counter and also the visited set(Dictionary thing) to confirm they are visited or not.

#
#
#
#
#

# 6-03-2026

'''Difference between the BFS and the level order traversal'''
#-> BFS is a general algorithm which is used for travesing the trees or the graphs level by level like meeting neighbourhood first
#-> Level order traversal is a speacial case of BFS which is used for only Binary trees.