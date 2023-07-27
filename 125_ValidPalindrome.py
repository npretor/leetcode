

def isValidPalindrome(s):
    s_ascii = ''.join([i for i in s.lower() if i in 'abcdefghijklmnopqrstuvwxyz0123456789'])  
    import ipdb; ipdb.set_trace() 

    if len(s_ascii) == 1 or len(s_ascii) == 0:
        return True 
    
    for i in range( int( len(s_ascii)/2 ) ):
        if s_ascii[i] != s_ascii[-i-1]:
            return False
    return True
            

s = " "    
print(isValidPalindrome(s) )