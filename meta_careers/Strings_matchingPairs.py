"""
Given two strings s and t of length N:
    find the maximum number of possible matching pairs 
    in strings s and t 
    after swapping exactly two characters within s
"""
from collections import Counter 

s = "abcd"
t = "adcb"

s = 'mno'
t = 'mna'


def matching_pairs(s, t):
    """
    Go through the strings, and see how many are different. 
    For the different ones, see if there is a version of that in the other 
    """
    if s == t:
        return len(s) - 2

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    matching_pairs = 0
    mismatch_indexes = []
    for i in range(len(s)):
        if s[i] == t[i]:
            matching_pairs+=1    
        else:
            # Either we track the mismatched appendices, 
            mismatch_indexes.append(i) 
            
            # Or we track the items that don't fit in two arrays 
    if matching_pairs == len(s)-1:
        return len(s) - 2

    # Now to see what should be swapped. 
    # Convert the characters to indexes in the alphabet, and make each pair a set 
    mismatch_pairs = []
    for idx in mismatch_indexes:
        mismatch_pairs.append( 
            set({ 
                alphabet.index(s[idx]), 
                alphabet.index(t[idx]) 
                }) ) 
    
    # Now we count the matching sets
    matches_so_far = 0
    for i, set_pairs in enumerate(mismatch_pairs):
        for j, compare_pairs in enumerate(mismatch_pairs[i+1:]):
            # print("i:  {}  j:  {}".format(set_pairs, compare_pairs))
            matches = 2 - len(set_pairs.difference(compare_pairs)) 
            if matches > matches_so_far:
                matches_so_far = matches
                
    # print("possible matches: ", matches_so_far)


    return matching_pairs + matches_so_far

print(matching_pairs(s,t))