# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        if not curr:
            return curr
        nextNode = curr.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nextNode
            if curr:
                nextNode = curr.next

        return prev
        
        