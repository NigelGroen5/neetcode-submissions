class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        res = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res


# we are going to move r 1 each time. add r count to count
# if r count is biggest we have, attempt maxf update
# if window size - maxf > k: we have more lost elements than supposed to
# then we will move left up 1, and -=1 count of l
# after doing that update res to max of window size and past
