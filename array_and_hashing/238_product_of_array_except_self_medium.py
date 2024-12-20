# Given an integer array nums, return an array answer such 
# that answer[i] is equal to the product of all the elements 
# of nums except nums[i]. The product of any prefix or 
# suffix of nums is guaranteed to fit in a 32-bit integer. 
# You must write an algorithm that runs in O(n) time and 
# without using the division operation.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize result array with 1's
        res = [1] * len(nums)

        # Calculate prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Calculate postfix product and update result
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
    
# Time: O(n)
# Space: O(1)