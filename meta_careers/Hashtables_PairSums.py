"""
Given a list of n integers arr[0..(n-1)], 
determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, 
each copy is considered to be different; 
that is, two pairs are considered different 
if one pair includes at least one array index 
which the other doesn't, 
even if they include the same values.
"""
from collections import Counter

# Assumptions: 
# 1. The list is not sorted 
# 2. 
# Hints: The value of the items is always smaller than the length of the list... why is that? 

arr = [1, 2, 3, 4, 3] 
arr = [1, 5, 3, 3, 3]
#arr = [10, 20] 

# Filter out items larger than k 


def numberOfWaysNaive(arr, k):
    ways = 0
    
    # Sort 
    arr.sort()

    for i, n in enumerate(arr):
        for item in arr[i+1:]: # we can do this because it's sorted 
            if k-n == item:
                ways+=1

    return ways 


def numberOfWaysHash(arr, k):
    ways = 0
    
    # Sort 
    arr.sort()
    c = Counter(arr) 

    for i, n in enumerate(arr):
        # Check for if we are searching for our value 
        if k-n in arr[i+1:]:
            ways+=1 
            # Decrement the value after search 
            c[k-n]-=1 
            print(c)
    return ways

print(numberOfWaysNaive(arr, 6)) 
print(numberOfWaysHash( arr, 6)) 