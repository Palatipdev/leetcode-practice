# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # approach one: 
        # make one variable walk until tail
        # keep one variable at the start
        # even / odd variable, even = counts 

        # actually approach one is inefficient because if we want to assign a tailEnd and need to decrement one each even "index" we would need to restart the walk which with be O(n) * O(n-1) * O(n-2) 

        # thing is, if we are using prev and curr method, we would need to keep track of the current prev, for example keep track of n-1 so that it can point to 1 and 0 and point to it

        # this is tricky but i feel like its the concept that i know of if we could access tail end and decrement it that would be very easy

        # fuck we just return a reverse linked list
        
        #  O(n) time O(1) space
        def findLength(head):
            count = 0
            curr = head
            while curr:
                curr = curr.next
                count += 1
            return count

        # O(n) time O(1) space
        def cut(head, count):
            curr = head
            for _ in range(1,(count + 1) // 2):
                curr = curr.next
            save = curr.next
            curr.next = None
            return save

        # O(n) time O(1) space
        def reverseListHalf(head):
            prev = None
            curr = head
    
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev


        
        
        count = findLength(head)
        tail = reverseListHalf(cut(head, count))
        curr = head

        while tail:
            tempCurr = curr.next
            tempTail = tail.next
            curr.next = tail
            curr = tempCurr
            tail.next = curr
            tail = tempTail
            
            

        # but we won't be able to count how many times until we overlaps two list and this is modifying two list to point at each other rather than one
        # change approach


        # but important distinction. Odd indexes = front increment / Even indexes = back decrement