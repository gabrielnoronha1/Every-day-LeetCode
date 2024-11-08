# Given an integer array nums, return true if any value
# appears more than once in the array, otherwise return 
# false.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()
        
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
            
        return False
    
# Time: O(n)
# Space: O(n)