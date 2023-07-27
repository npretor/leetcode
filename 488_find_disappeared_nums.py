

def disappeared(nums):
    all_n = [n for n in range(1, len(nums)+1)] 
    s_nums = set(nums) 

    return list(set(all_n).difference(s_nums))


assert disappeared([4,3,2,7,8,2,3,1]) == [5,6] 
