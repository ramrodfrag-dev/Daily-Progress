

"Zip function:" # combines elements from multiple iterables based on their index and returns tuples.

a = [1, 2, 3]
b = ['a', 'b', 'c']

print(list(zip(a, b)))
# Output
# [(1, 'a'), (2, 'b'), (3, 'c')]
# How it works:
# a[0] + b[0] → (1, 'a')
# a[1] + b[1] → (2, 'b')
# a[2] + b[2] → (3, 'c')        We can also do for x,y in zip(a,b)
    

# Time: O(1)        if there are n elements then time complexity becomes O(n)
# Space: O(1)       if zip is converted to list then space complexity becomes O(n)

# so, basically it does not stores anything just it iterates and pack each index element as one

# ->What happens if length of each list is different
names = ["John", "Alice", "Bob", "David"]   # list → 4 items

grades = (85, 90, 78)                       # tuple → 3 items   ← shortest

letters = "ABCDE"                           # string → 5 characters

result = zip(names, grades, letters)
print(list(result))

#Output:
# [('John', 85, 'A'),
#  ('Alice', 90, 'B'),
#  ('Bob', 78, 'C')]

"zip() stops when the shortest iterable ends"

#
#
#
#
#
#
#

"Anonymous Function" #->There are just one time functions
result = list(map(lambda x: x * x, [1, 2, 3]))              #Ex:1

# Unlike normal functions which can be used any number of times once initialized but this can be only used once when initialized.

square = lambda x: x * x                #Ex:2
print(square(5))

"lambda input: operation"               #->This is the format how the lambda is written
lambda x: x * 2                 #Ex:3
lambda x: x + 10
lambda x: x % 2 == 0
lambda x: x[0]

# It is also used when we are doing the sorting things we use this inside a inline function:

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

intervals = [(0,30),(5,10),(15,20)]
intervals.sort(key=lambda x:x.start) #type:ignore
# or
dicts={1:3,5:6,-1:7}
dicts=sorted(dicts.items(),key=lambda x:x[1]) # Here we get the output as list instead of dict as it is sorted and based on key it is being sorted.

# Note: dictionary does not have sort function which others have.

" The important thing is that sorted() itself always returns a new list, regardless of whether you're sorting tuples, objects, dictionaries, strings, etc,"
"while the .sort sorted the elements inplace instead of creating new structure, but only some data structure have .sort and for others like dictionaries we have to use sorted function "

#
#
#
#
#
#

"Set default in dictionaries"

# Ex:
timeMap={}
key="an"
value,timestamp="jan",3
timeMap.setdefault(key,[]).append((value,timestamp))
# Instead of first creating the list if it is empty by checking and then appending.
# is not recommedable as starts the thing by the default value if it is not initialized until now.



"How the functions are written:"

class Node:
    def __init__(self, x: int, next: "Node | None" = None): # Here next can be Node or None
        self.val = int(x)
        self.next = next
        
# see how the default values are written.

def sum(a:int,b:int)->int:
    return a+b

# See how the return values are written in code