# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # merge first and second half.
        # find middle
        s, f = head, head
        while f and f.next:
          s = s.next
          f=f.next.next
        
        second = s.next
        s.next= None

        # reverse second
        prev = None
        while second:
          temp = second.next
          second.next = prev
          prev = second
          second = temp
        
        curr = head
        while curr and prev:
          tempS = curr.next
          tempP = prev.next
          curr.next = prev
          prev.next = tempS
          curr = tempS
          prev = tempP

          