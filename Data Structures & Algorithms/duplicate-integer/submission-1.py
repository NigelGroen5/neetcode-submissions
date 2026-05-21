class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set(nums)
        print(len(vals), len(nums))
        if len(vals) != len(nums):
            return True
        return False
        