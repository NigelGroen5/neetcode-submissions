# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      if not lists or len(lists) == 0:
        return None
        
      # while lists has more than 1
      while len(lists) > 1:
        mergedLists = []
        # iterate in groups merging them
        for i in range(0, len(lists), 2):
          list1 = lists[i]
          if i+1 < len(lists):
            list2 = lists[i+1]
          else:
            list2=None
          mergedLists.append(self.mergeTwoLists(list1, list2))
        lists = mergedLists
      return lists[0]
      
    def mergeTwoLists(self, a, b):
      dummy = ListNode()
      curr = dummy
      while a and b:
        if a.val < b.val:
          curr.next = a
          a = a.next
          curr = curr.next
        else:
          curr.next = b
          b = b.next
          curr = curr.next
      if a:
        curr.next = a
      if b:
        curr.next = b
      return dummy.next

