
# Recursion is nothing but a function which calls itself.

'''Factorial''' #Others: Fibanacci numbers, finding depths of trees and lists,etc

class Soln:
    def Factorial(self,n):
        if n==1 or n==0: return 1
        else:
            return n * self.Factorial(n-1)
        
obj=Soln()
print(obj.Factorial(5))

# Remember when calling a function in the class add self before that instead of adding another argument like self.
#
#
#
#
#

# Fibanacci series:
''' 0, 1, 1, 2, 3, 5, 8, 13, 21'''

#
#
#
#
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root=TreeNode()

# Finding depth of tree
def recurse(root):
    if not root: return 0
    
    left=recurse(root.left)
    right=recurse(root.right)
    return max(left+1,right+1)
def main():
    count=recurse(root)
    return count
# Here add root nodes and check its value