import random 
import time 

r = random.randint(0, 2**31) 

def guess(g):
    if g == r:
        return 0 
    if g > r:
        return -1
    if g < r:
        return 1 
    

def guessNumber():
    """
    Start out 
    """
    low = 1 
    high = 2**31 
    mid = int((high-low)/2) 

    while True:
        print('current guess:\t', mid, "\tactual:\t", r)  
        time.sleep(0.25)

        # If guess is correct: 
        if guess(mid) == 0:
            return mid 
        
        elif guess(mid) == 1:
            # Your guess is too low
            low = mid 
            mid = mid + int((high-low)/2)

            
        elif guess(mid) == -1:
            # Your guess is too high
            high = mid
            mid = mid - int((high-low)/2)


print('success: ', guessNumber())