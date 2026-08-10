# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative
        stack = []
        n = 0 
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                


            
            x = stack.pop()
            n+=1
            

            if n == k:
                return x.val

            curr = x.right
                
        
            