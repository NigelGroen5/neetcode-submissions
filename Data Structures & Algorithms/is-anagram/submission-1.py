class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        hss = {}
        hst = {}
        for i in s:
            if i in hss:
                hss[i] +=1
            else:
                hss[i] = 1
        for i in t:
            if i in hst:
                hst[i] +=1
            else:
                hst[i] = 1
        return hss == hst

#trial 1
#time: O(n^2)
#space: O(1)

#trial 2:
#time: O(n + m)
#space: O(n)