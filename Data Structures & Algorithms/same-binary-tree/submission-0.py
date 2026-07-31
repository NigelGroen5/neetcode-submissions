# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#          self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      # dfs recursive
      # check roots the same, continue or return false
      # if do match: check if childs are same
      # more base cases: 2 null nodes, return true
      # right node null left not, return false
      # both not null: check values
      # my predictoin: O(n), O(n) - call stack
      # real
      # time: size of both trees bc worst case iterate every node in both O(p+q)
      if not p and not q:
        return True
      if not p or not q or p.val != q.val:
        return False

      return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))



# ask: are all these questions binary trees
# ask: insight to realize this