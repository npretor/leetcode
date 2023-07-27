
def containsDuplicate(nums: list[int]):
        # Make this faster by making a set as we go. Check to see if each item is in the set
        # c = Counter(nums)
        # for item in c:
        #     if c[item] > 1:
        #         return True 
        
        # This is faster 
        s = set() 
        s.add(nums[0])
        for item in nums[1:]:
            if item in s:
                return True 
            s.add(item)
        return False


print (containsDuplicate([2,14,18,22,22]))
