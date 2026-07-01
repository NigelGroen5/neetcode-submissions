class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        max_length = 0 
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            max_length = max(max_length, len(charSet))
        return max_length