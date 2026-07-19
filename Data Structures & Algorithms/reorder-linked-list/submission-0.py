# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #merge 2 halves toghether. 
        slow, fast = head, head

        while fast and fast.next:
          slow=slow.next
          fast = fast.next.next
        #slow is at the middle now, reverse slow side of list
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
          temp = curr.next
          curr.next = prev
          prev = curr
          curr = temp
        # merge curr and first half
        while head and prev:
          temphead = head.next
          tempprev = prev.next
          head.next = prev
          prev.next = temphead
          head = temphead
          prev = tempprev

        