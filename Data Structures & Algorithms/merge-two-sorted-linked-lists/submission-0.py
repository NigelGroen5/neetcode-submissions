# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 Null, and list2 isn't, return list2
        # if list2 Null, and list1 isn't, return list1
        # if both are NULL, reutrn Null
        # Else: 
        # compare list1.val and list2.val
        # attach whichever node has smaller val to the result
        # move that list's pointer forward by one
        # repeat until one list runs out
      currOne = list1
      currTwo = list2
      newList = ListNode() # ****
      currNew = newList

      while currOne and currTwo:
        if currOne.val <= currTwo.val:
          currNew.next = currOne
          currOne = currOne.next
        elif currOne.val > currTwo.val:
          currNew.next = currTwo
          currTwo=currTwo.next
        currNew = currNew.next
      if currOne:
        currNew.next = currOne
      if currTwo:
        currNew.next = currTwo
      return newList.next
        

      