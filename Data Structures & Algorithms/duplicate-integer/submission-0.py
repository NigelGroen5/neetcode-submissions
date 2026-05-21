class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counted = []
        for i in nums:
            if i not in counted:
                counted.append(i)
            else:
                return True
        return False