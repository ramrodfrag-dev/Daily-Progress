"How to get all the possible string with a certain number of characters by repetation and fixed length"

def bt_dfs(path, n, result):
    if len(path) == n:
        result.append("".join(path))        # this is base condition where we need to stop
        return

    for char in ["A", "B"]:
        path.append(char)
        bt_dfs(path, n, result)     # Here we will traverse from through invisible tree and build tree and store values. See the pic in reference pics for more info
        path.pop()          # Here pop is necessary because it is the root of backtracking of how to change the decisions we have taken earlier and make new ones later.


result = []
bt_dfs([], 2, result)       # Here the result remains same and the empty array is used as temporary stack and it gets updated continuously.

print(result)

# See here how each time one element is placed and goes to check for others and later pops


# 29-09-2026(Day 31)


# ============================================================
''' BACKTRACKING - QUICK NOTES'''
# ============================================================

# MAIN IDEA:
# Choose -> Explore (DFS) -> Undo choice
#
# Typical pattern:
#
# make a choice
# dfs(...)
# undo the choice
#
# Example:
# path.append(x)      # CHOOSE
# dfs(...)            # EXPLORE
# path.pop()          # UNDO / BACKTRACK


# ============================================================
# 1. SUBSETS - TAKE / DON'T TAKE
# ============================================================

# Use when every element has 2 choices:
#   1. Take
#   2. Don't take
#
# Each element can be used only once:
# -> both branches move to i + 1

def subsets(nums):
    res = []
    path = []

    def dfs(i):
        # Every element has been decided
        if i == len(nums):
            res.append(path.copy())
            return

        # TAKE
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

        # DON'T TAKE
        dfs(i + 1)

    dfs(0)
    return res


# ============================================================
# 2. SUBSETS WITH DUPLICATES
# ============================================================

# IMPORTANT:
# Sort first so duplicates are together.
#
# In TAKE/SKIP style:
# Skip duplicate values in the SKIP branch.

def subsetsWithDup(nums):
    nums.sort()
    res = []
    path = []

    def dfs(i):
        if i == len(nums):
            res.append(path.copy())
            return

        # TAKE
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

        # SKIP all duplicates of current value
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1

        dfs(i + 1)

    dfs(0)
    return res


# ============================================================
# 3. COMBINATION SUM
# ============================================================

# Can reuse the SAME element multiple times.
#
# TAKE -> dfs(i)       # stay at same i, can reuse
# SKIP -> dfs(i + 1)   # move to next element

def combinationSum(nums, target):
    res = []
    path = []

    def dfs(i, total):
        if total == target:
            res.append(path.copy())
            return

        if total > target or i == len(nums):
            return

        # TAKE -> reuse allowed
        path.append(nums[i])
        dfs(i, total + nums[i])
        path.pop()

        # SKIP
        dfs(i + 1, total)

    dfs(0, 0)
    return res


# ============================================================
# 4. COMBINATION SUM II
# ============================================================

# Every element can be used only ONCE.
#
# TAKE -> i + 1
# SKIP -> i + 1
#
# Sort + skip duplicates.

def combinationSum2(nums, target):
    nums.sort()
    res = []
    path = []

    def dfs(i, total):
        if total == target:
            res.append(path.copy())
            return

        if total > target or i == len(nums):
            return

        # TAKE
        path.append(nums[i])
        dfs(i + 1, total + nums[i])
        path.pop()

        # SKIP duplicates
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1

        # DON'T TAKE
        dfs(i + 1, total)

    dfs(0, 0)
    return res


# ============================================================
# 5. PERMUTATIONS
# ============================================================

# Order matters.
#
# At every level:
# Try EVERY unused element.
#
# Use a FOR LOOP because there are many possible choices,
# not just TAKE / DON'T TAKE.
#
# Must use ALL elements before saving answer.

def permute(nums):
    res = []
    path = []
    used = set()

    def dfs():
        if len(path) == len(nums):
            res.append(path.copy())
            return

        # Try every unused element
        for num in nums:
            if num in used:
                continue

            # CHOOSE
            path.append(num)
            used.add(num)

            # EXPLORE
            dfs()

            # UNDO
            path.pop()
            used.remove(num)

    dfs()
    return res


# ============================================================
# 6. GENERATE PARENTHESES
# ============================================================

# Choices:
#   Add '('
#   Add ')'
#
# But only valid choices are allowed.
#
# '(' can be added if open < n
# ')' can be added if close < open

def generateParenthesis(n):
    res = []
    path = []

    def dfs(open_count, close_count):

        # Complete valid answer
        if open_count == n and close_count == n:
            res.append("".join(path))
            return

        # Add '('
        if open_count < n:
            path.append("(")
            dfs(open_count + 1, close_count)
            path.pop()

        # Add ')'
        if close_count < open_count:
            path.append(")")
            dfs(open_count, close_count + 1)
            path.pop()

    dfs(0, 0)
    return res


# ============================================================
# MASTER RULES
# ============================================================

# 1. WHEN TO USE i vs i + 1?
#
# Can reuse current element:
#     dfs(i)
#
# Can use current element only once:
#     dfs(i + 1)


# 2. WHEN TO USE FOR LOOP?
#
# Use FOR LOOP when:
# "At this position, I can choose ANY one of many choices"
#
# Examples:
# - Permutations
# - N Queens
# - Sudoku
# - Standard combination generation
#
# Example:
#
# for choice in choices:
#     choose
#     dfs()
#     undo


# 3. WHEN TO USE TAKE / DON'T TAKE?
#
# Use when every element has exactly 2 choices:
#
# TAKE:
#     path.append(nums[i])
#     dfs(...)
#     path.pop()
#
# DON'T TAKE:
#     dfs(...)


# 4. WHEN TO SAVE ANSWER?
#
# All elements / positions must be completed:
#
# if i == len(nums):
#     res.append(path.copy())
#
# OR
#
# All elements must be used:
#
# if len(path) == len(nums):
#     res.append(path.copy())
#
# OR
#
# A condition is achieved:
#
# if total == target:
#     res.append(path.copy())


# 5. DUPLICATES
#
# Usually:
# nums.sort()
#
# FOR LOOP STYLE:
#
# for j in range(start, len(nums)):
#     if j > start and nums[j] == nums[j - 1]:
#         continue
#
# This skips duplicate choices at the SAME recursion level.


# ============================================================
# UNIVERSAL BACKTRACKING TEMPLATE
# ============================================================
'''
def backtracking_template():

    def dfs(state):

        # 1. BASE CASE
        if solution_found:
            save_answer()
            return

        # 2. TRY CHOICES
        for choice in choices:

            # Skip invalid choices
            if invalid:
                continue

            # 3. CHOOSE
            make_choice()

            # 4. EXPLORE
            dfs(next_state)

            # 5. UNDO
            undo_choice()

'''
# ============================================================
# FAST DECISION GUIDE
# ============================================================

# Does every element have YES / NO?
#     -> TAKE / DON'T TAKE
#
# Can reuse the chosen element?
#     YES -> dfs(i)
#     NO  -> dfs(i + 1)
#
# Do I have many possible choices at each level?
#     -> FOR LOOP
#
# Does order matter?
#     YES -> permutations / use unused elements
#     NO  -> combinations / move forward with start index
#
# Are duplicates present?
#     -> sort + skip duplicates
#
# What must be true before saving?
#     -> all elements used?
#     -> reached end?
#     -> target reached?
#     -> valid board/string?
#
# ALWAYS REMEMBER:
#
#       CHOOSE
#         ↓
#       DFS
#         ↓
#       UNDO
#
# append/add -> dfs -> pop/remove
# ============================================================


# 29-08-2026 (Day 32)

''' Word Search '''

# Leetcode: 79

# Here a matrix of all characters are given. So, we need to return true is a given word is present when traversed from sidewise or vertical sideways.
# So, we use dfs and first we traverse all elements if there is a first character then we search for second letter in its neighbour and if it is found it recursively calls for 3rd letter and so, on.
# Remember to push elements to visited and pop from it as each letter can be used for only once. And we should not return if there is immediate rejection of letter, we have to seach for all letters, while using the moments array.
#Ex:
'''def search(row,col,i):
            if i==len(word):
                return True
            for dr,dc in movements:
                r,c=row+dr,col+dc
                if (r in range(rows) and
                c in range(columns) and
                (r,c) not in visited and
                board[r][c]==word[i]):
                    visited.add((r,c))
                    found=search(r,c,i+1)
                    if found:
                        return True
                    visited.remove((r,c))'''    #Remove if this(i) does not lead to next letter(i+1) because we can get the same letter(i) in one its other neighbour, and then we can go though and get all other characters.
                    
                    



'''Palindrome Partioning'''

# Leetcode: 131

# -> Always rememeber if we do our work correctly at current instant then all child calls will do correctly irrespectiver of anything.
# Here we need to return all the subset of palindrome which are palindrome and we check all possible subsets of every divison. see question for clarity.
s= "aab"
res=[]
result=[]
Output= [["a","a","b"],["aa","b"]] # see all the subsets of each division is given, it is nothing but in how many ways it can be divided.

def dfs(i):
    if i>=len(s):
        result.append(res.copy())
        return
    
    for j in range(i,len(s)):
        if ispalin(s,i,j):  #type:ignore
            res.append(s[i:j+1])
            dfs(j+1)
            res.pop()
        
dfs(0)
print(result)

# See how this works in refernce_pics(Palindrome partioning)
# We need to first take one element and see if it is palindrome and next take first 2 elements and check palindrome or not and so on until whole string. If in all these if a given string is palindrom then add to subset and then recursively call itself and finally pop for backtrack.
# Clear soln: https://www.youtube.com/watch?v=3jvWodd7ht0




'''N Queens: LeetCode-51'''

# Here a number is given and then we are asked to find all possibilities of placing queen. We use backtrack and check at each position we can place a queen or not.
# So, while traversing for each row we will place one queen and then move forward. so, storing rows is unnecessary. Things to store:
# 1.Columns-In which columns other queens are present
# 2.positive Diagonal-In which positive diagonal previous queens are  present.
# 3.negative Diagonal-In which negative diagonal previous queens are present.

####Note:
#->1.Positive Diagonal: It is the diagonal whose slope is +ve.
# How to identify: Their sum of row and column will be same for all cells in that diagonal as when going upwards right col value increases and row value decreases.
#So, (r+c) is same for all cells in a particular positive diagonal.

#->2.Negative Diagonal: It is the diagonal whose slope is -ve.
# How to identify: Their difference of row and column will be same for all cells in that diagonal as when going downwards right col value increases and row value increases.
#So, (r-c) is same for all cells in a particular negative diagonal.


# By storing these values apply all column checks using backtracking. Remember to add the values and then call recursively and later delete values to backtrack properly.

n=4
board=[['.']*n for i in range(n)]
res=["".join(x) for x in board]

# See how to intialize the nxn matrix with all '.' and then update required accordingly.


