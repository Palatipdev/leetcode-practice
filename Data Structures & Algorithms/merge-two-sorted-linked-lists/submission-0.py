# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1

        dummy = ListNode(0)
        current1 = list1
        current2 = list2
        tail = dummy


        while (current1 != None and current2 != None):
            if (current1.val >= current2.val):
                tail.next = current2
                tail = tail.next
                current2 = current2.next
            else:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
        if (current1):
            tail.next = current1
        else:
            tail.next = current2
        return dummy.next
        