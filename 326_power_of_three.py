



# Check if a number is a power of three


def checkRecursive(n):
    # Check if the number divided by three is 1 AND if the number modulo 3 is zero 
    # If the number divided by three is greater than 1, keep going  
    print(n)
    # Base case 
    if n / 3 == 1 and n%3 == 0:
        return True 
    
    if n/3 < 1:
        return False
    
    if n/3 > 1:
        return checkRecursive(n/3)

print(checkRecursive(28))    