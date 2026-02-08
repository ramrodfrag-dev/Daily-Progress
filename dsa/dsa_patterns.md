

<!-- 27-01-2026 -->

PATTERN: Two Pointers

When to use:
- sorted array
- Palindrome checks
- In-place Modifications

Why it works:
- Reduces nested loops
- Avoids Extra memory



<!-- 28-01-2026 -->

PATTERN: Sliding Window

When to use:
- When we want to process a subset of data
- If we are asked to find longest substring or subset following some conditions

Why it works:
- It works because we update the left and right points according to the conditions and get the required result instead of creating new structure for storing it.


Note: Difference between 2 pointers and sliding window
- Sliding window is a part of 2 pointers approach. In 2 pointers the pointers can move in any directions and solving a relationship problem whereas in sliding window we use pointers in such a way that it maintains a valid range and adjusting it's size.



<!-- 30-01-2026 -->

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



<!-- 2-02-2026 -->

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




<!-- 5-02-2026 -->

PATTERN-1: How to access methods and variables of another methods inside a same class.


PATTERN-2: Range Update Tricks

Used When:
- When we are asked to updates many contigous elements each time for many queries which take O(n) for each query to execute.
### - Range Updation Problems

Key idea:
- Relativeness of elements from one to other mostly they see relativeness with the previous element

Implementation in python_core_practice.py




<!-- 6-02-2026 -->

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





<!-- 7-02-2026 -->

PATTERN:

Used when:

Key idea: