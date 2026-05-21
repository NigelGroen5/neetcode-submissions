class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # what matters?
        #chars = chars
        #hash table frequencies are equal
        
        #creates a hash table for string s.
        if len(s) != len(t):
            return False
        ss = {}
        for char in s:
            if char in ss:
                ss[char] += 1
            else:
                ss[char] = 1
        tt = {}
        for char in t:
            if char in tt:
                tt[char] += 1
            else:
                tt[char] = 1

        return ss == tt

        