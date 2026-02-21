
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

