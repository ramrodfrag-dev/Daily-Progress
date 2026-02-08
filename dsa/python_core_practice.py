# there will be all functions which I have learned including with comments of their explaination



#26-01-2026

# General
ord('c') # will get you the ascii value of that character used for arithmatic operations
chr(98) # will get the character associated with the number


# Dictionaries:

student={'rollno':'23bcs071','branch':'CSE','Institute':'IIITDWD'}

student.get('rollno') #same as the student['rollno'] which gets the values
student.update({'rollno':'23BCS071','phno':'1234567890'}) # can get any arguments this updates the dictionary
student.pop('phno')  #same as the del student['phno'] but it gives the value after deleting unlike del function which does not give

for key,value in student.items():  # here items() is same as enumerate function
    print(key,value)
    
student.items() # will give you all keys and values in stuent
student.keys() # will only give keys
student.values() # will only give values

# Note: Do not use .pop() function inside a loop as it only takes O(n) so we will finally get O(n^2)
#       Instead use some other 2 pointer or different approach to do it.
string="hello I am a hero"
# for i in string ->This will give you each character
# for i in string.split()  ->This will give you each word


# Leet Code: 283->Moving zeroes to last and 387->Find Index of first unique character in string

#283:
# process followed is first add non-zero elements at beginning and later add i.e. update zeroes to finnally fill remaining zeroes. Take any variable and Increase when a value is updated from beginning to end.

#387:
#Took a dictionary and added all counts of characters in it and later found the index of character by again iterating through the string.




#27-01-2026


#General
#In computer science, an in-place algorithm is an algorithm that operates directly on the input data structure without requiring extra space proportional to the input size. 


# 2 pointer Approach:
#This type of approach is used when storing will become an issues.
'''
There are majourly 3 types of 2 pointers thing:
1.Converging Pointers: Used when we want to check both ends simulataneously and further come. Ex:Checking Palindrome,max Water Container
2.Parallel Pointers: Used when Right pointer is to find extra Info about left one and left one for progress. Ex:Sliding Window
3.Trigger-based Pointers: First one pointer finds one required thing and then another pointer finds additional info about it. Ex:Finding last to nth node in linked list
Some other things are Fast-Slow pointers used specifically inlinked list to find chains,etc 
'''


#LeetCode: 125->Valid Palindrome and 26->Remove Duplicates from sorted Array

#125:
#Here I took 2 points and when the character at that pointer is neither a alphabet or a nemerical I have moved pointers if not I have compared the two values and checked whether they are unequal or not. If Unequal retrun False else return True.

#26:
#I took 2 pointes one indexed at 0 and other indexed at 1 if I see same number on both the pointers then I increase the right pointer otherwise I increase the left pointer and add the number at right pointer and then increase the right pointer.

'''Suggestion:
Before submitting any LeetCode solution, ask:
1)What does the function return?
2)Is modification in-place or returned?
3)Are there input constraints I ignored?
4)Did I move pointers every iteration?'''




#28-01-2026

#General

# Sliding Window
''' There are 2 types of sliding window:
1)Fixed Sliding Window ->size remains same. Used when we want to find a fixed given length of array results or string ones
2)Dynamic Sliding Window   ->size changes based on the condition. This is used when we need shortest or longest substrings in strings or a particular larger or small consequtive value in the arrays thing.'''

''' sub=sub[1:] ->This is used to remove the 1st character in the string.'''

'''Note: Always do not include everything in a single loop. if needed use 2 seperate loops as we need minmum number of executions must happen. like one may run for 5 and other for 10 so, we can save time for 5 statement condition checking things.'''

#LeetCode: 3->Longest Substring without repeating characters and 643->Maximum average value sub array

#3:
#Here I have first taken 2 pointers and increased right when there is new character and increased left when there same character in the substring until the right pointer character is no longer a duplicate. This is sliding window approach move
#pointers and update the substrings to get the unique characters in a substring without any duplicates. Here substring is stored and used for checking the next character is available or not, instead of hashing. This is dynamic sliding window.
'''array=array[1:] which takes all the elements in to array except the first one.''' #This is used as popping 1st element 

#643:
#Here also I used the sliding window approach and first I moved right arrow untill the give window size is met and then incremented the left and right at the same time to maintain the window size and meanwhile calculating the sum of the window.
#This is the fixed sliding window.



#29-01-2026 ->Skipped due to excess assignments of vcc and devsecops

#30-01-2026

#General

#key=lambda x:x[1] means we are making the second set of elements as keys like if the dictionary is {"a":1,"b":2} here keys are generally a,b but if we do the following command then we are saying consider x[1] as key i.e. not x[0] so 1,2 are keys now.
#This applies for the command.
unique={}
sortedList=sorted(unique,key=lambda x:x[1],reverse=True)  #Here x contains a,b and if we do x[1] then error occurs
sortedList=sorted(unique.items(),key=lambda x:x[1],reverse=True) #Here x contains (a,1)(b,2) so x[1] means take 1,2 as keys instead of a,b. so that we can sort them by keys
#Understand like if we do unique in for loop we only get keys but if we do unique.items() then we will get bith keys and pairs then we can choose which to become the keys for sorting

#Note:
'''dict(sorted(array))  this is general one which sorts and provide as dictionary. we can also add parameters like key, reverse,etc. But for array.sort() no parameters can be added and it can be used for list but not for dictionaries.'''


#LeetCode: 3->Longest Substring without repeating characters and 347->Top k frequent Elements

#347:
#Used general formula for knowing frequency and later I sorted the list based on x[1] as key and with descending order and finally stored only the top k values of the sorted dictionary and returned the value.
num=[1,1,1,2,2,3]
unique[num]=unique.get(num,0)+1          #->general formula here for getting frequency of the given array or list or any other and form a dictionary with that.

#3:Again Updated from yesterday like adding the hashing in it for fast accessing.
#Here used the hashing that is dictionaries and checked the characters are present in the window or not instaed of using the strings for checking it which takes O(n) time but now it takes O(1) time for checking but for deleting some characters it takes O(n)


#Extra 49: Group Anagrams -> combine all anagrams together

strs=["eat","tea","tan","ate","nat","bat"]
def anagram(strs):
    group={}

    for word in strs:
        st="".join(sorted(word))

        if st not in group:
            group[st]=[]

        group[st].append(word)

    return list(group.values())

# Here Observe the grouping thing and do not over think it. when they are saying group them by anagrams then their sorted words will be same or their frequency will be same. So, first make dictionaries with these content and then sort them with values and later
# group them with respect to values pair and all keys come together and make a list and return them. but here null strings duplicates will be removed and answer goes wrong
'''Instead think simply''' # and just make group dictionaries and add the lists which conatins values(st) as keys and keys(word) as values and then we print all values to get the group values(word) together. see above code for reference.





# 01-02-2026    -> Gone like a waste day somehow




#02-02-2026


#General:
# Studied about Big O notatiion and which sort has what worst time comparision. Reference: https://www.bigocheatsheet.com/


#LeetCode: 121->Best time to buy and sell stocks and 238->Product of Array except self

# 121:This stocks repeats many time but this is basics. Again I have done over engineering. JUst forgot the point that stocks can be sold after buying only and tried to search both min and max values and checked whether the buyed date is before sold date and stuff
'''Correct Way''' # This is simple. First take a min value which is inf and maxiProfit value as 0 anf then traverse though the array and then update the minvalue such that it is minimum of both (min,price) and then the maxiProfit which is to be the maximum of 
#(maxProfit,price-min) which finally gets to the maxiProfit which can be aquired. This is possible because always we sell after we buy so at eaach iteration we calculate the min value and maxProfit we can get from that.If you do not understand take pen and paper and visulaize by drawing an array on it.

# 238:This process is very important and can be asked at many times in arrays concepts. Here in order to calculate the product or sum of all the elements in the array except the elements at that index we use this method.
'''Steps to follow'''
#First take result array which is same length as that of the main given array and then put all 1s in it as they asked product of elements expect those of that index and if sum is asked then place all 0s. Now keep a for loop and update the result array by taking a prefix variable along with it. Like:

nums=[1,2,3,4,5]
result=[1] * len(nums)
prefix=1

for i in range(0,len(nums)):
        result[i]=prefix
        prefix*=nums[i]


suffix=1

for i in range(len(nums)-1,-1,-1):
    result[i]*=suffix
    suffix*=nums[i]
    
#So, as we can observe the result array is updating first with the prefixes in it and then it is being updated by the suffixes of it as we know suffix*prefix. This is what the logic is.






#3-02-2026

#General:
'''Think Simply Just observe what data structure is required and then just plug in that, do not overthink or any other things. Do'nt do over Engineering, Just please think simply for easy questions.'''

#Leetcode: 345->Reverse Vowels in a String and 680->Valid Palindrome-II

#345:
# Here first I have overthinked it but see carefully. First we came to know that we have to use 2 pointers as we have to replace the vowels in the string. For that understand as string is immutable first we covert string to a list and the loop in the list and place 2 points r and l such that l waits
# at starting vowels and r waits at the last vowel and then move r and l in for loops such that they always stop and vowels untill r>l and then swap them. After everything we just convert the list to the string by "".join(arr) and return it.

#680:
# Here this is a palindrome question where we check if it is a palindrome or not it is a palindrome even if one of the character is removed from the string.
#Ex: abca is a palindrome as removing b or c will make it a palindrome. So, I put a function which tells the given string a palindrome or not by taking a string part. It is done like sending the function r,l which points towards the substring we are trying to check it. Next we take while loop until right>left
# and see the s[r]==s[l] if they are equal then its fine but if it is not then call the function like ispalin(left+1,right) || ispalin(left,right+1) so, if any of these is true then the outcome will be true and we know it is a palindrome if we remove one letter from it.



#5-02-2026

#General
'''Something Related to OOPS and classes'''
class NumArray:

    def __init__(self, nums: list[int]):    # see self is include in that method
        self.prefix=[0]

        for i in range(0,len(nums)):
            self.prefix.append(nums[i]+self.prefix[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
    
# Observe the code carefully see if one function or variable which is being initialized or written in one method of a class is to be accessed by another method of the same class then use self before that variable or method always and also include self in the methods while initializing



#Leetcode: 303->Range Sum Query Immutable and  598->Range Addition

# 303: It is just the prefix sum concept just only the classes and how to use self when some variables of one method is called by another method is known now. It is like adding a self tag infront of it just like self.variablename to call and access it.

#598: This is very easy one after reading the entire question and operations being performed we need to find number of elements in the matrix with the highest value in it. We are given with a m*n matrix and all are initialized by zeros then we perform all operations on it and after clearly
# -reading question carefully by any operations the the 1st element is going to change or not changed so max will be always in (0,0) and number of elements which are similar to (0,0) are the only highest numbers but the array is not there as a input. SO, I have to manipulate the m,n and 
# the operations such that I get the reqired number. It is simple just maths like x=min(op[0],x) and calculate y similarly and if both are ot equal then x*y is the required number if not do some manipulations to result.


'''Note: Most Important Concept so far -> Range Updates problems with many complex operstions to perform for a contiguos elements in a array'''

# Here instaed of blindly applying the opertions to the array everytime and with huge numbers takes lot of time so, we generally use the concept of relativity.
# Relativity means for ex: how much variation is the element 2 is from element 1 and how much variation is the element 3 is from element 2 and so,on. So if we are performing the same operations to all the contiguous elements then their relative changes will only observed in 2 places like 
# -stating of the contiguous sub array and the ending of it

#EX:

nums=[1,5,10,15,25]
#If the operation to perform is to add +5 to all elements from index(l,r) i.e from index l to r where r>=l
#Our approach here looks like below
relativeness=[1,4,5,5,10,0] # Like here first element is same and second element is 4+first element so we get 5 and third element is 2nd element + the current relativeness form 2nd and so,on

# 0 at last is a dummy for updating when the last number is said to be updated

#Now if the changes are made then i.e +5 assume form index 2 to 4. Then the relativeness list will be:

relativeness=[1,4,10,5,10,-5] 
# Here only l index will be added the value and then in index r+1 the same value will be deducted to show it became more less after the previous number is added
# Finally remove the last dummy number and find the original how they are updated by this and return just like how we made relativeness form the actual array.





# 6-02-2026

#General:

'''Difference between subarray, subsequence and subset:'''
# If we have{1,2,3,4} then the 
# Subset can be {1,4}, {1}, etc It can be in any order and any number of numbers
# Subarray can be {1,2,3}, {2,3,4}, {2,3} but not {2,4}
# Subsequence can be {2,4}, {1,3,4}, {1,4} but not {4,1}


#Leetcode: 15->3Sum problem and 560->Subarray Sum Equals k

#15: It is given given the array we need to find the triplets whose sum is equals 0.
#Method used: First sort array so that all duplicates numbers can be found and also 2 pointers approach can be used. So, after sorting iterate a loop for 1st element of triplet in array and then use 2 pointers such that left pointer must start just after the 1st element and the right pointer must start from end of array.
# Now,check if the elements at the points and the element currently in the outer loop adds to target(0) if yes add this list to triplets or else if the sum is +ve then decrement the right pointer by 1 if r>l and if the sum is less than 0 then increment the left pointer by 1 if l<r and continue untill l<r.
# Note: Also beaware of the duplicates thing if right and left pointers find any duplicates while values are changing then remove duplicates before adding in to the triplets by skipping like if x>0 and sum[x]==sum[x-1] then continue without doing anything. x is 1st number in outer loop and z,y are left and right pointers.

#560: Here subarray means contiguous non-empty sequence so, at first glance we think use sliding window but its not the case
# Concept used: Here there are 2 concepts that can be used one is for +ve numbers and one for both +ve and -ve numbers

'''Only for +ve numbers and 0's'''
# Here we can use the sliding window method to solve this increase the window size if the sum<key (or) even if the right<len(nums) and then update the sum by new sum and continue in the loop and then if sum>key then decrease the size of the window from beginning and then update the sum by deleting the first number of the list and move forward
# Also at last remember to increase the left pointer that is shrink the window size so that it also checks subarrays which ends with last element of array but starts with any of the element in the array. And also remember to break the loop.
# This is the optimal soln for only +ve numbers

# Whatever Data structure you use or how many loops you use you cannot make a sliding window work for the -ve numbers. It's a fact.

'''Both for +ve, 0's  and -ve numbers'''
# Here we can use the hashing tables and prefix sum concepts to solve this in optimal time. So, we know the best we can do normally is outer loop runs for once for each sub array starting from it and the inner while loop takes consideration for where it ends and we calculate sum and if sum reaches k then we increase counter otherwise no. so, complexity is O(n^2) for sure.
# To make it optimal we should make it in O(n) so, we should not have 2 loops inside of one other. so, Here we use reverse Engineering. Instead of using array we use prefix sum as we need to travel array once so, we need to keep track of how much sum untill now so that we do not need to calcuate once more.
# So, first we add this curent index number to sum. If the sum==k then count++, if it is not check if there exists a subarray which has sum-k as its sum so, we get to know that from that point to current is a subarray of k so, we can increase the count. Then place current prefix sum to hash along with count variable like if you found this sum for first time then keep 1 as
# count otherwise fetch that count and increase by 1 and replace it.
'''Implementation is important:'''
def subarraySum(self,nums: list[int], k: int):

    hashe={}
    sum=0
    count=0
    
    for i,num in enumerate(nums):
        sum+=num
        if sum==k:
            count+=1
            
        if sum-k in hashe:
            j=hashe.get(sum-k)
            count+=j
        
        if sum not in hashe:
            hashe.update({sum:1})
        else:
            j=hashe.get(sum)
            hashe.update({sum:j+1})

    return count






# 7-02-2026

#General


# Leetcode: 

#

#