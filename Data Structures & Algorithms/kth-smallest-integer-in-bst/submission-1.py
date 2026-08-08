# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      self.count = 0
      self.k = k
      self.result = None
      self.inOrder(root)
      return(self.result)
        

    def inOrder(self, root):
      if not root or self.result is not None:
        return 
      
      self.inOrder(root.left)
      
      self.count += 1
      if self.count == self.k:
        self.result =  root.val
        return

      self.inOrder(root.right)

