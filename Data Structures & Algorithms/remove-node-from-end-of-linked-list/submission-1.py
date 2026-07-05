# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the linked list
        # then from there start counting from 1 as head then +1 when next

        dummy = head
        fast = head
        slow = head
        output = []
        for i in range(0,n):
            fast = fast.next
        if fast != None:
            while fast.next != None:
                fast = fast.next
                output.append(slow)
                slow = slow.next
            slow.next = slow.next.next
            return dummy
        else:
            return head.next
        
        