class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            # skip duplicates
            if i > 0 and v == nums[i-1]:
                continue
            # 2 pointers. rearrange equation -1*i = j+k
            l, r = i+1, len(nums) -1
            key = -1*v
            while (l<r):
                value = nums[l] + nums[r]
                if value == key:
                    res.append([v, nums[l], nums[r]])
                    # append match then skip duplicates and move to next value
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif value < key:
                    l += 1
                elif value > key:
                    r -= 1
            
        return res
