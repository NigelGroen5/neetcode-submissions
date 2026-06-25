class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        maxS = 0
        for i in numSet:
            if i-1 not in numSet:
                curr = 1
                while (i+1 in numSet):
                    curr +=1 
                    i += 1
                maxS = max(maxS, curr)
        return maxS