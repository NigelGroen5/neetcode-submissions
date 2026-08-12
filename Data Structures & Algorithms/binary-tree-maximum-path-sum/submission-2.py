# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # global var for result set to value at root
        # list bc can modify it in recursive function?
        res = [root.val]

        # return max path sum without splitting
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            #update incase negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute max path sum WITH split
            # take root value and add with left and right max
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return value is max of this without splitting
            # can't choose both bc that means we are splitting
            return root.val + max(leftMax, rightMax)
            
        dfs(root) #updates res value
        return res[0]


        
