# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
          return

        # find middle

        s, f = head, head.next
        
        while f and f.next:
          s = s.next
          f =f.next.next

        new = s.next
        s.next = None # cut connection bw halves

        # reverse new second half
        prev = None
        while new:
          temp = new.next
          new.next = prev
          prev = new
          new = temp
        
        curr = head
        # merge
        while prev and curr:
          temp_curr = curr.next
          temp_prev = prev.next
          curr.next = prev
          prev.next = temp_curr
          curr = temp_curr
          prev = temp_prev
        



