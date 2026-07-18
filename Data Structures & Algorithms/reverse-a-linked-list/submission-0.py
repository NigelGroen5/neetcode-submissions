# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr=head
        while curr:
            next_temp = curr.next # save rest of list 
            curr.next = prev # reverse this node's pointer
            prev = curr # move prev forward
            curr =next_temp # move curr forward
        return prev # prev ends up as the new head

# O(n) O(1)