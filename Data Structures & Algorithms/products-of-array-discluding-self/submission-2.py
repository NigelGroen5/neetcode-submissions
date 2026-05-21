class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1] * (len(nums)+1)
        suffix = [1] * (len(nums))
        
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res

