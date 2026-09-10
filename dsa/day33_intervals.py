
# 10-09-2026 (Day 33)

"Insert Intervals" # LeetCode->57

# We are given with some Intervals which are non,overlapping and ascending with respect to the starting points. We need to insert a new Interval which is also given into this nd do the merging if necessary.
# Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

#Intuition:
# See what cases may possible:
# Case 1: new_Interval is before the current Interval
# ->Here we append the new_Interval to result and then all the other Intervals
# Case 2: new_Interval is after the current Interval
# ->Here we append the current and then wait to see the next Interval comes after new_Interval or it is merging. so we just append current and then iterate the loop
# Case 3: It is merging
# ->may be the new_Interval is between the current Interval or it may merge in the beginning or at the end or it may cover whole Interval and still has many elements left.
# Note: 
#   Do not think how to merge it's complex and what about these all merge cases, just take the 3 merge case example from case 3 and try to solve it.
#   We get like the merge Interval starting is the minimum of new_interel and current Interval and the end is the max of current Interval and the new_Interval.

# Note: In these Interval questions while looping use the range function instead of the enumerate function because we can get more uses out of it like:
# ->we can directly return by adding other Intervals after a new_Interval is inserted which cannot be done in eneumerate function as it needs to loop until last to get all the Interval in the Intervals array.

def insert_Interval(intervals:list[list],newInterval:list):
    res=[]
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])

        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
            
intervals = [[1,3],[4,6]]
newInterval = [2,5]
print(insert_Interval(intervals,newInterval))





"Non Overlapping Intervals" # LeetCode ->435


# Here all intervals are given and if there are overlapping ones then we have to return the number of intervals we need to remove to get all non-overlapping intervals.
# Here we can use the Back propagation thing as we can include one interval once and then remove it and check for others. As we have 2 options for each one we end up with exponential time.
# Better is greedy as we can delete the ones which end later than the ones which ends before for the sorted intervals.(Comparing adjacent intervals after sorting)
# This can be done by sorting the intervals with starting points and then comparing end points or using them oppositely.

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
    intervals.sort()
    count=0
    prev=intervals[0]

    for i in range(1,len(intervals)):
        if prev[1]<=intervals[i][0]:
            prev=intervals[i]
        else:
            if prev[1]>=intervals[i][1]:
                prev=intervals[i]
            count+=1
    return count


