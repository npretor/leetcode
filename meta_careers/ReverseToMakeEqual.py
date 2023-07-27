from collections import Counter 


a = [1, 2, 3, 4]
b = [1, 4, 3, 2] 

a_2 = [1, 2, 3, 4]
b_2 = [1, 2, 3, 5]  

tests = [
    [a,b],
    [a_2, b_2],
    [[2],[1]],
    [[None],[1]],
    [[], []],
    [None, None]
]


def testEqual(ac, bc):
    if ac == None or bc == None:
        if ac == None and bc == None:
            return True
        else:
            return False
        
    if ac == [] or bc == []:
        if ac == [] and bc == []:
            return True
        else:
            return False

    if len(ac) is not len(bc): 
        return False 
    
    
    if Counter(ac) == Counter(bc):
        return True
    else:
        return False


t = 0
for test in tests:
    if testEqual(test[0], test[1]):
        print("case {} success".format(t))
    else:
        print("case {} failed".format(t))
    print("  ",test[0], test[1])
    t+=1
