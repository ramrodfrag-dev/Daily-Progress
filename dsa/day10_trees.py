
import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This is for the Level Order Traversal for any binary or any other tree

class Solns:
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







# 22-08-2026 (Day 28)

"Lowest Common Ancestor in Binary Search Tree"
# LeetCode: 235

# Here a Binary search tree(all elements to the left of root is smaller than root and all elements to the right of root are larger) is given.
# so if immeadiate ancestor must be returned
#Ex:
root = [5,3,8,1,4,7,9,None,2]   # Draw this and understand how it works
p,q = 3,8
output=5

root = [5,3,8,1,4,7,9,None,2]
p,q = 3,4
output=3

####Soln:
# Use the fact this is a binary search tree and if the both p,q are on one side of root then check that side or otherwise return root

def ancestor_finder(root,p,q):
    while True:
        if p.val<root.val and q.val<root.val:
            root=root.left
        elif p.val>root.val and q.val>root.val:
            root=root.right
        else:
            return root
# We can also do it in the recursion format by calling the root.right or left according to the conditions instead of while loop.

#
#
#
#
#

# 23-08-2026 (Day 29)

"Count Good nodes in binary tree"

# Leetcode:1448

# Here they asked about the total no.of nodes whose value is greater than equals to all the nodes values from top of root until them.
# Generally We will think of the dfs as they need to traverse depth wise to check node along with parent.
# So, we use this in our favour and keep one more parameter i function and add the required parameter in function in order to remember and calculate using this value without forgetting in the recursive way.
### Important:
# The only way to make the algorithm remember the values which are needed for them to calculate result and also they change when traversing is the adding parameter way and using the return statement.
# Ex:
def counts(self,root:TreeNode,h:int)->int: #type: ignore
        if not root:
            return 0
        curr=root.val
        h=max(curr,h)
        l=self.counts(root.left,h)
        r=self.counts(root.right,h)
        if root.val>=h:
            return l+r+1
        return l+r

def goodNodes(self, root: TreeNode) -> int:  #type: ignore
    res=self.counts(root,root.val)
    return res

#
#
#
#
#

"Check the valid BST"

# The Best way to do it by using the Inorder traversal, but if we use list in each point and concatent them and send to parent it becomes tle.
#### Soln:
# We use an array throughout the recursions and all operations change this array only.
'''Remember: When an array is passed and updated in a recursion its state is not changed '''
class Node:
    def __init__(self, val, right=None):
        self.val = val
        self.right = right

def dfs(root, arr):
    if not root:
        return
    print("Current root:", root.val)
    print("Before append:", arr)
    arr.append(root.val)
    print("After append:", arr)
    dfs(root.right, arr)

# Tree: 1 → 2 → 3
root = Node(1, Node(2, Node(3)))

arr = []
dfs(root, arr)

# see the code clearly when the value changes in the function then only it creates multiple objects and keep one for each recursive loop
# But if the parameter is not changed at all i.e by just adding and deleting the elements, there will be a shared memeory of that object and it can be used outside of the recursive call also.

'''Every recursive function call creates a new stack frame with its own local variables and parameters. When we call dfs(root.right, arr), the new recursive call gets its own local root reference pointing to root.right,
while the previous call's root remains unchanged. However, arr in every recursive call can refer to the same list object. Therefore, operations such as arr.append() modify that shared list, and the changes remain even after the recursive call returns.
Returning removes the inner function's stack frame, but it does not undo modifications made to a shared mutable object.'''

# Representation:
 
# Call 1                 Call 2                 Call 3
# root → Node 1          root → Node 2          root → Node 3

# arr ─────────────┐
#                  │
# arr ─────────────┼────→ [1, 2, 3]
#                  │
# arr ─────────────┘





"Best Way to traverse the tree and get the elements by order and store them:"       # Remember

class Soln:
    def dfs(self,root: Optional[TreeNode], arr: list):
        if not root:
            return
        self.dfs(root.left,arr)
        arr.append(root.val)
        self.dfs(root.right,arr)
        
    def main(self,root: Optional[TreeNode]):
        res=[]
        self.dfs(root,res)
        
        
        
        
# 24-08-2026 (Day 30)

"Construct Binary Tree from Preorder and Inorder Traversal"

# Leetcode: 105

# Here we are given with a preoder and a inorder traversal list and we know some facts like:
# 1.The order of elements in preorder will be like the root,left,right in this.
# 2.The order of elemets in inorder will be like the left,root,right in this.

#->The first element in the preorder traversal will be the root of the root then left and right,
# so then find this element in the inorder and note that index and all elements before this index will be the right side of the root and right side all elements belongs to right side of the root.

## Code:
class Solutions:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
# But it may give the TLE in some case for big inputs because continously we are slicing and the then finding index every time.
# To avoid tle follow the below code by taking the dictionary and the keeping extra variables to point out to arrays instead of slicing:
class Solution:
    def buildTree(self, preorder, inorder):

        pos = {}

        for i, value in enumerate(inorder):
            pos[value] = i

        preIndex = 0

        def dfs(left, right):
            nonlocal preIndex

            if left > right:
                return None

            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            mid = pos[rootVal]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
