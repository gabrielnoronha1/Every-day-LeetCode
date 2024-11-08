# Given two strings s and t, return true if t is an anagram 
# of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for j in count_s:
            if count_s[j] != count_t.get(j, 0):
                return False

        return True

# Time: O(n)
# Space: O(k)