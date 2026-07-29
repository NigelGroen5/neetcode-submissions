class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while (l<=r):
          mid = (l+r) // 2
          if nums[mid] == target:
            return mid
          # check both halves for which is sorted
          # if nums target < mid: decide based on l,r
          if nums[l] <= nums[mid]:
            if target >= nums[l] and target < nums[mid]:
              r = mid - 1
            else:
              l = mid+1
          else:
            if target <= nums[r] and target > nums[mid]:
              l = mid+1
            else:
              r= mid-1
        return -1