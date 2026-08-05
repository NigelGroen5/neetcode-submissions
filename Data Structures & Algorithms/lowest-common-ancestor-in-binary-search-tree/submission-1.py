# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        if not curr:
          return None

        while curr:
          # if both are to the left: move left. same with right
          # if not, theres a split, return curr
          # if both to left
          
          if curr.val > p.val and curr.val > q.val:
            curr = curr.left
          elif curr.val < p.val and curr.val < q.val:
            curr = curr.right

          else:
            return curr
