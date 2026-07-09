class Solution:
   def minWindow(self, s: str, t: str) -> str:
       # edge case of empty t
       if t == "":
           return ""

       countT  = Counter(t)
       window = defaultdict(int)
       have, need = 0, len(countT)
       res, resLen = [-1, -1], float("inf")
       l = 0

       for r in range(len(s)):
           window[s[r]] += 1
           # if freq of curr char matches desired count in T, increment count
           if s[r] in countT and window[s[r]] == countT[s[r]]:
               have += 1
               
           #shrink the window from left as long as it remains valid
           while have == need:
               # save smallest window up to now
               if (r-l+1) < resLen:
                   res = [l,r]
                   resLen = r-l+1
               # decrement left, if removing it break conditions decrement have count
               window[s[l]] -= 1
               if s[l] in countT and window[s[l]] < countT[s[l]]:
                   have -= 1
               # move left to match reality
               l += 1

       # return smallest window or empty string if no window exists
       l, r = res
       if resLen != float("inf"):
           return s[l:r+1]
       else:
           return ""
     
# complexity:
# space: O(s+T): store char frequencies in dicts. O(n)
# time: O(s+t): every char in S is visited at most twice. O(n)
