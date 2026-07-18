# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case, no next node is empty or curr is empty(edge case): return head
        if not head or not head.next:
            return head
        
        # 
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

# O(n) O(n)