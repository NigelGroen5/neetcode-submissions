class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_seq = 0

        for i in numSet:
            curr = 1
            if i-1 not in numSet:
                while i+curr in numSet:
                    curr += 1
            max_seq = max(max_seq, curr)
        return max_seq