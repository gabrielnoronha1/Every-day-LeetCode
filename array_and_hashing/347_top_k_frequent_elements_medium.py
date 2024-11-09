# Given an integer array nums and an integer k, return the k
# most frequent elements. You may return the answer in any 
# order.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        # List of lists where index represents frequency, 
        # stores numbers by their frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count occurrences of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Group numbers by their frequency in the freq list
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Gather top k frequent elements from high to low 
        # frequency
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Stop once we have k elements
                if len(res) == k:
                    return res

# Time: O(n)
# Space: O(n)