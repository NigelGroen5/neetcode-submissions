class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        countT = Counter(t)
        have, need = 0, len(countT)
        window = defaultdict(int)

        res =[-1, -1]
        resLen = float('inf')

        l=0 

        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        if resLen == float('inf'):
            return ""
        else:
            return s[l: r+1]