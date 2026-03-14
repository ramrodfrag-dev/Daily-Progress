

## 27-01-2026

PATTERN: Two Pointers

When to use:
- sorted array
- Palindrome checks
- In-place Modifications

Why it works:
- Reduces nested loops
- Avoids Extra memory



## 28-01-2026

PATTERN: Sliding Window

When to use:
- When we want to process a subset of data
- If we are asked to find longest substring or subset following some conditions

Why it works:
- It works because we update the left and right points according to the conditions and get the required result instead of creating new structure for storing it.


Note: Difference between 2 pointers and sliding window
- Sliding window is a part of 2 pointers approach. In 2 pointers the pointers can move in any directions and solving a relationship problem whereas in sliding window we use pointers in such a way that it maintains a valid range and adjusting it's size.



## 30-01-2026

PATTERN: Hashing

Use when:
- Frequency counting
- Duplicate detection
- Fast lookup

PATTERN: Sliding Window + HashSet

Use when:
- Substring problems
- Longest / shortest window



PATTERN: Grouping by Signature (Hashing)

Use when:
- Anagrams
- Categorization problems

Key idea:
- Same signature → same group



## 2-02-2026

PATTERN: Prefix-Postfix Sum or product

Defination: Used to find the sum or product of all the elements except those of that position. Ex: Arr=[1,2,3,4] result=[24,12,8,6] ->This is for the Product.

Used When:
- Product except self
- Range sum queries
- Trapping rain water
- Left max / right max
- Stock profit problems
- Sliding window optimizations

Key idea:
- Prefix = past
- Suffix = future
- Current element = ignored

Implementation see in the python_core_practice.py




## 5-02-2026

PATTERN-1: How to access methods and variables of another methods inside a same class.


PATTERN-2: Range Update Tricks

Used When:
- When we are asked to updates many contigous elements each time for many queries which take O(n) for each query to execute.
### - Range Updation Problems

Key idea:
- Relativeness of elements from one to other mostly they see relativeness with the previous element

Implementation in python_core_practice.py




## 6-02-2026

PATTERN: Frequency Map
- It consists of HashMap and also prefix sum for optimal soln.

Used when:
- If problems mentioned about subarray
- If it asks count of subarrays
- Longest subarray with sum k
- When Sliding window fails(It fails for -ve numbers as inputs)

Key idea:
- take hashmap and update it with prefix sum as the keys and the values can be anything depending on the question.
- Value can be count if they need all subarrays with length k
- Value can be index if the size of the longest substring with k as sum is asked.





## 7-02-2026 (Day8)

PATTERN: Monotonic Stack(Decreasing or increasing ones)

Used when: We we need to find the:
- next greater element(Monotonically Decreasing Stack)
- next smaller element(Monotonically Increasing Stack)
- previous smaller element(Monotonically Increasing Stack)
- previous greater element(Monotonically Decreasing Stack)
- Questions similar to these concepts

Key idea(For monotonically decreasing): We take an stack(list) and loop through the list given:
- If current iterating eleemnt > stack[-1] then pop the stack and continue until current element < stack[-1].
- If it comes out of above while loop then push the current element in to the stack. And continue until all elements are covered in main list given.
- After popping update the results by adding the current element to the result to the appropriate result index




PATTERN: Finding min,max element of the given stack at a particular time.

Used when:
- If the stack max,min element is asked in O(1) time

Key idea:
- Take an other stack(minstack or maxstack) and collect the elements which are max or min up to that layer of stack.
- even if the above layers vanish also we have max,min in each layer which calculates up to that layer starting from bottom.





## 10-02-2026(Day9)

PATTERN: Deque

Used When:
- wants the addition or deletion of elements fromt the starting.
- when adding and deleting thousand numbers in to a list

Key idea:
- from collections import deque
- q=deque()
- Other implementations are in practise_py files.

Note:
- Lists when the space is completed it doubles it size and then copies the elements in to it and while deleting also if space is more it becomes half and like that.
- so, time is significantly wasted
- In case of deque the time is not wasted because the deque is just like a linked list. So, if a new item comes it just allocates a new space and head is changed accordinglly.


Note:
Syntax:
- root:Optional[TreeNode] ->This means root datatype can be either of Treenode or None.
- Here TreeNode is not defned. You can define it in any way.




## 11-02-2026(Day10)

PATTERN: Level-by-Level Traversal(Use BFS for traversal) -->Use Queue

Used When:
- When tree data structures are given or the problem is solved by BFS Algorithm

Key idea:
- Outer loop for the deque to be empty and inner for the length of the deque. This traverses like BFS and here use level_items variable to catch all variables before running while loop again



## 16-02-2026(Day11)

PATTERN: Recursion

Used When:
- When we require function to call itself again and again with different variable values

Key idea:
- We generally have a base case which terminates the recurseive call in a stack and pops it -->Base case
- And recursive call which calls itself -->Recursive step

Note:
- Always define variables in a class and use it in all methods or just use return statement to get the variables updated instead of just creating new variables again and again in the recursive stack



## 26-02-2026(Day12)

PATTERN: Depth-First-Search(DFS) -->Use Stack

Used When:
- When tree data structures are given or the problem is solved by DFS Algorithm

Key idea:
- It is recursive type of thing, which calls itself instead of bfs which is iterative in nature



## 11-03-2026

PATTERN: Fibonacci Series

Key idea:
- Use the fibanocci thing by recursion

Note:
- if the recursion takes too long resulting in the TLE then use the DP pr a similar process to store and retrive repeating calculated data 
- In DP there are 2 things: 1. Top to down approach which takes larger time and large call stack space 2. Bottom to top approach which is usually better as it uses iteration instead of the Recursion

When to use this:
- When the result of current elements depend on other elements and they are the same question but the input is less
- Climbing Stairs
- House Robber



## 12-03-2026

PATTERN: Heaps

Key idea: -> we use arrays for this heap
- It is a complete BinaryTree which can be implemented by using arrays instead of node structures and pointers which consumes more memory
- Arrays takes O(logn) for adding or deleting items, whereas in node types it takes O(n)for finding element+O(logn) for adding or deleting

Note:
- left child will be there in (2*i)+1 where i is the parent
- right child will be there in (2*i)+2 where i is the parent
- parent node will be (i-1)//2 where i is the child of the parent

When to use this:
- Top K elements (K largest, K smallest) or frequent elements
- Priority scheduling or next available worker
- Shortest path
- Repeated best choices(Pick smallest or largest or next best)
- When numbers continuously come and we need to maintain the min,max of the numbers

Implementation and other info see in day13_heaps.py



### PATTERN: Bucket Sort

Key idea:
- Here we make everything in to buckets and then each value is placed in to certain bucket and then the buckets are placed in the correct order
- For each bucket there will be a list in which we add elements so, we need more space.
- The time complexity is O(n) as just we are placing elements to each bucket and then putting all buckets at once in their same order.

When to use:
- when the given elements are in a certain range not very huge(must be small)
- when there are more like frequency things


### PATTERN: Tim Sort

Key idea:
- Here we are mixing both the merge and insertion sort
- First divides all sorted and unsorted like some parts to make only changes in the unsorted parts
Ex: [1,2,3,7,6,5,8,9]
first sorted runs like [1,2,3,7], [6,5], [8,9]
second it uses the insertion sort and sort the unsorted things
finally merges those combinely at last
- Time complexity is O(nlogn) which is greater than most algorithms but optimal for most of the items that needs to be sorted. so this is general .sort() uses.

When to use:
- General .sort() uses this method. we generally do not use specifically as it is not optimal for a particular things instead it is optimal for all general case.




