class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        window = {}

        while (l<r):
          if nums[l] < nums[r]:
            return nums[l]
          mid = (l+r) // 2
          if nums[mid] > nums[r]:
            l = mid +1
          else:
            r = mid
        return nums[l]
          

'''
if at left is bigger than right = check left vs middle
if at left is smaller than right = its nums[0]
'''