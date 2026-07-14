class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        maxL = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+= 1
            maxL = max(maxL, r-l+1)

        return maxL
