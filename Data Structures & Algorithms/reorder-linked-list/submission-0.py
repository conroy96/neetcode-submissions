# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        tmp = slow.next
        slow.next = None
        slow = tmp 
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        first = head
        second = prev
        while first and second:
            tmp1,tmp2 = first.next,second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        





        
        
        
        
        
            
            
        

        