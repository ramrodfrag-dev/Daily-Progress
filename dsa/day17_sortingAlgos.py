
''' Topological Sorting:'''

# Used only for Directed Acyclic Graph(DAG).
# -> Linear Ordering of vertices such that for every directed edge u->v, vertex u comes before v in the order.
# Ex: 5->0, 4->0, 5->2
# Sol: 5,4,0,2 and 5,4,2,0 and 4,5,0,2 and 4,5,2,0 and 5,2,4,0. All answers are correct
# So, in this type of sorting there is no such thing that there should be a fixed answer there may be any no. of answers.


"How to sort Objects"

# If the elements which we want to sort are integers or list of integers or list of characters or worders then normal .sort works
# what if the elements we need to sort are the list of objects which contain integers.
# Ex: 
# Definition of Interval:
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

# so, other than normal lists and numbers we need to use the lambda function just like the dictionaries but we need to specify what element we need to consider in the data structure to sort.
# Here we use the start variable so we do like:

intervals = [(0,30),(5,10),(15,20)]
intervals.sort(key=lambda x:x.start) #type:ignore


