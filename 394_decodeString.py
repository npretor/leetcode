# Do this brute force 

s = "3[a]2[bc]" 


def decodeString(s):
    strings = {} 
    inside_bracket = False 

    for char in s:
        if s.isdigit():
            strings[s] = [] 

        
        



assert decodeString(s) == "aaabcbc"