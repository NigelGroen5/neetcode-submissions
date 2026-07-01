class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i + 1, len(nums)-1

            while (l<r):
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -=1
                    while nums[r+1] == nums[r] and l<r:
                        r-=1
                    continue
                
                elif threeSum > 0:
                    r -= 1
                
                elif threeSum < 0:
                    l += 1
                
        return res