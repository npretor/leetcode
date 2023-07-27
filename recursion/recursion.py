"""
Helpful stuff 
1. Find the simplest possible input 
2. What is the repeating pattern? Is the pattern comprised of sub-patterns? 

"""



def r_sum(n):
    """Sum all non-negative integers to n"""
    # Base 
    if n == 0:
        return n 
    
    # Recursive 
    else:
        return r_sum(n-1)+n 
    

def grid_paths(x, y):
    """ How do I print this? """ 
    if x==1 or y==1:
        return 1
    else:
        return grid_paths(x, y-1) + grid_paths(x-1, y) 


def partition_permutation(n, m):
    """
    Write a function that counts the number of ways you can partition n objects using parts up to m (assuming m ≥ 0) 
    
    """
    print("I don't even know what that question is asking ") 

if __name__ == "__main__":
    # print(r_sum(10)) 

    paths = grid_paths(3,3)
    print(paths) 