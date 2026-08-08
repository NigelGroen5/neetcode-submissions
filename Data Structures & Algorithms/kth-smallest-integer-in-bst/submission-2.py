# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive and iterative. O(h+k) O(h)
        
        #recursive
        self.k = k
        self.result = None
        self.count = 0
        self.inOrder(root)
        return self.result

    def inOrder(self, root):
        if not root or self.result is not None:
            return None

        #recurse left
        self.inOrder(root.left)
        
        self.count += 1
        if self.count == self.k:
            self.result = root.val

        self.inOrder(root.right)


