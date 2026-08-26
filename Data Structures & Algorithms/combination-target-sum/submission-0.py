class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # i = index in nums we're deciding on
        # curr = combination built so far
        # total = running sum of curr
        def dfs(i, curr, total):
            # if path hits target
            if total == target:
                res.append(curr.copy()) # copy bc keep using curr var
                return 
            # if path greater than target
            if i >= len(nums) or total > target: 
                return 
            
            # two choices, at index i two things you can do 
            # 1: include it
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            curr.pop()
            # 2: skip it
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res




