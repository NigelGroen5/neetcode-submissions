class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]

        while (l<=r):
          # if left less than right its sorted, update res and end loop
          if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
          
          mid = (l + r) // 2
          res = min(res, nums[mid])
          # if mid greater than l means right has min
          if nums[mid] >= nums[l]:
            l = mid + 1
          # else move right
          else:
            r = mid -1
        return res
