# Given an array of strings strs, group the anagrams 
# together. You can return the answer in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        
        for s in strs:
            # Count characters using a fixed-size list, 
            # creating a unique signature for each anagram 
            # group
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            
        return list(res.values())
    
# Time: O(m * n)
# Space: O(m)