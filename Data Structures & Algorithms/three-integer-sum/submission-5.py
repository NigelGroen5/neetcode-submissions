class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        res = []

        for i, v in enumerate(numbers):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            l, r = i+1, len(nums) -1
            key = -1*v
            while (l<r):
                value = numbers[l] + numbers[r]
                if value == key:
                    res.append([v, numbers[l], numbers[r]])
                    while l < r and numbers[l] == numbers[l + 1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif value < key:
                    l += 1
                elif value > key:
                    r -= 1
            
        return res
