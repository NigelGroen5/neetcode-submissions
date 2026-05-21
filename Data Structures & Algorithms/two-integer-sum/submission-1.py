class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in seen:
                return[seen[key], i]
            seen[nums[i]] = i
