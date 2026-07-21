class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = defaultdict(int)
        countT = Counter(t)
        res = float('inf')
        resLen = [-1,-1]
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
          countS[s[r]] += 1

          if s[r] in countT and countS[s[r]] == countT[s[r]]:
            have += 1
          
          while have == need:
            if r-l+1 < res:
              res = r-l+1
              resLen = [l, r+1]

            countS[s[l]] -= 1
            if s[l] in countT and countS[s[l]] < countT[s[l]]:
              have -= 1
            l += 1
        if resLen == [-1, -1]:
          return ""
        return s[resLen[0]: resLen[1]]


