class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total): # i = index we at, curr, total sum
            # if total matches target
            if total == target:
                res.append(curr.copy())
                return True


            if i >= len(nums) or total > target:
                return
            curr.append(nums[i])

            
        
            # we know that index is valid and total is less than target
            
            # keep going with current value, it will either add to res or not, but pop so can go next
            dfs(i, curr, total+nums[i])
            curr.pop()

            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res
            




