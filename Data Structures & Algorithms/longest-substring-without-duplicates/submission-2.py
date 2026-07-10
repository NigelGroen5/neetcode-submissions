class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l = 0
        count = set()

        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            maxL = max(maxL, len(count))
        return maxL

# O(n): go through string once
# O(1): if everything is distinct theres only finite ascii chars