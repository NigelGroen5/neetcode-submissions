class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i,v in enumerate(nums):
            if target - v in n:
                return [n[target-v], i]
            n[v] = i
