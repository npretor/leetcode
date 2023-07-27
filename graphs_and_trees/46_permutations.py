from itertools import permutations 

def permute(nums):
    return([list(i) for i in permutations(nums)]) 


if __name__ == "__main__":
    print(permute([1,2,3])) 