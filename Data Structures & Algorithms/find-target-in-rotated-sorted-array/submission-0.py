class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while (l<=r):
          mid = (l+r) // 2
          if target == nums[mid]:
            return mid

          # if left value is less than or equal to middle, the entire left half is normally sorted
          if nums[l] <= nums[mid]:
            #  is target out of zone? move left up
            if target > nums[mid] or target < nums[l]:
              l = mid + 1
            # if inside, move right down
            else:
              r = mid - 1
          # rotation drop off is on left
          else:
            # is target outside right zone? serarch left
            if target < nums[mid] or target > nums[r]:
              r = mid - 1
            # inside update left
            else:
              l = mid + 1
        return -1



