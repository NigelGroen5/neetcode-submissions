class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            pre[i] *= prefix
            prefix *= nums[i]

        result = [1] * len(nums)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]


        print(result)
        print(pre)
        for i in range(len(result)):
            print(result[i], "*", pre[i])
            result[i] *= pre[i]
        return result