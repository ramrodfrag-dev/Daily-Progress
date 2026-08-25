

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




## 14-03-2026

PATTERN: 2 Heap problems

When to use:
- When there will be a stream of data and we need to find a medium or min or max values from coming values.

Key idea:
- 




## 22-06-2026

PATTERN: Multi-BFS Algorithm

When to use:
- When there will be more than one starting point in the bfs thing so we can do bfs at same time for all starting nodes.

Key idea:
- It is not complex just intially take many roots in the queue and then while removing instead of just keeping the while loop we also use the for loop along with the while in order to track the time elasped.




## 25-06-2026

PATTERN: Floyd's Algorithm

When to use:
- When finding cycles in linked lists or finding the start of the cycle if cycle exists.

Key idea:
- 2 points one move fast and one moves slow so they come together at some point later if cycle exists.

Reference:
- https://www.geeksforgeeks.org/dsa/floyds-cycle-finding-algorithm/



## 27-03-2026

PATTERN: XOR with the array numbers to find the unique number in pairs of numbers.

When to use:
- WHen there is only one unique number and all other numbers have their duplicate that is in pairs(2, 4 times).

Key idea:
- XOR operation with a number twice will givee the same result again initial

 Ex:
- If the initial answer is 0 and then we did XOR with 2 and later 3 and then 2 then the final result will be equals to 0 XOR with 3.
- So, Twice XOR with 2 cancells out and gives the same result as before.


## 2-08-2026

PATTERN: Valid Palindrome 2.

When to use:
- When they asked to find whether the given string is palindrome or not if atmost 1 character can be deleted.

Key idea:
- first use 2 pointers approach and see the given string is a palindrome or not and then if there is a mismatch then skip the two characters one ata time and check whether the remaining is palindrome or not.(Only one pointer give a movement and see remaining and see for the rest)

 Ex:
- abca. Here if we delete the b or c then we will get the palindrome approach using above idea.


## 3-08-2026

PATTERN: Palindrome by splitting.

When to use:
- specific problem is given in the: https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/SPLITPAL

Key idea:
- First keep two pointers left and right among them which is bigger split it and the same part keep it inplace of the bigger number and then extend the string and put that remaining number beside of current number.

 Ex:
- if the array is: [1,7,6,1,1] Here the 7 can be split into 6 and 1 as it is bigger than 6 when checking. Now both are equal at each pointer checking them and it will be a palindrome.



## 7-08-2026(Day19)

PATTERN: Prefix Product.

When to use:
- specific problem is given in the: https://neetcode.io/problems/products-of-array-discluding-self/question

Key idea:
- If they asked about all the sum or product except self then first make a left array with all prefixes and right array with all suffixes.Remove rightmost element in the left array and the left most element in the right array and finally multiple each element of lrft to the right and store in result array

 Ex:
- if the array is: [2,3,4,5] then the left=[1,2,6,24] and the right=[60,20,5,1] then the result=[60,40,30,24].



PATTERN: Circular Queue or array or anything

What to use:
- When the question says like what is the minimum no of the left shifts or the right shifts we need to make the element will be equalls to the index of the array -1based indexing.

Key idea:
- Use the Modulo operator(%) so that the next number again comes in the other side of the queue.
- To know the no. of steps an element(which is between 1 and length of array) to go to reach its index is: 
- k=(i-num)%n    #i-num or num-i is both fine
- res=min(k,n-k)  Here among k,n-k one is from the right side and the other is from left side. so check min distance and go for it.

Ex:
- arr=[5,3,2,1,4] Here with just one left shift 5 meets 5 index or with just 1 right shift 3 meets its index, so answer is 1.



## 8-08-2026(Day20)

PATTERN: TwoSum-II

What to remember:
- Just one thing whenever there are two pointers thing comes first keep left at 0 and right at end and do processing if not possible then in other cases do left at start and right at left+1. When sorted array is given always put the left at the start and the right at the end and make changes in those.


## 12-08-2026(Day21)

PATTERN: k closest elements

When to use:
- when they ask about return all those elements which are very near to the element given and also number of elements to print also given.

Key idea:
- When the total arr elements are less than the asking number of elements then print all elements, if the given element(x) is less than the first element of the array then print first k elements in array, print last k for the controversy thing.
- then if the given elemnt is between the elements then move to that index(i) and record it and later. make 2 pointers left=i-4 and right=i+4 if those are valid indexes otherwise make those max or min indexes of array,
- lastly put a while loop and it runs until right-left+1>k and check left and right element which is farther to the x remove that index and move further

Ex:[1,2,3,4,5,6,7,8], x=4, k=3
now as 4 is in middle of list then record i which will become 3(index) and now left=0,right=6,last while right-left+1>3: update left,right


PATTERN: Best time to buy and sell stocks

When to use:
- If there is a siustion where some item prices is mentioned in all those day and you can buy and sell then what is max_profit,we can use.

Key idea:
- Always remember the max_profit=max(max_profit,price-min_price) as the price daily we will check and update min_price until then and see what will be the max_profit if they sell that that specific day.So, daily the max_profit and min_price will be updating.




## 23-08-2026(Day29)

#### Some basic things to rememeber:

- To check whether a tree is a Valid Binary Search Tree or not, the best way is to derive its inorder traversal and 
see all the elements are in increasing or not. For it you need to use the recursive stack type approach and pass a variable to get the values instead of returning all lists which may cause tle

- When the '+' operator between two numbers is performed the addition happens and when it is done between the strings then the concatenation takes place but when it is done between the lists the lists gets added up. But if the both operands given are not of the same datatype then it throws an error as it cannot perform operation.

- When we use the enumerator it starts the indexing from 0 whatever array you give and however you split.
 Ex: enumerate(arr[1:]) this gives from 1st index only but the indexing starts from 0.
 So, in order to remove this confusion just use the range() or other functions when indexes are important along with nums in arr instead of the enumerate function.



 