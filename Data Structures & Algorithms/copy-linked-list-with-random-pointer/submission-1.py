"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        dummy = Node(0)

        first = head
        if head is None:
            return None
        pointer = Node(first.val)
        dummy.next = pointer

        copies = {first: pointer}
        first = first.next
        while first:
            pointer.next = Node(first.val)
            copies[first] = pointer.next

            pointer =pointer.next
            first = first.next
        first = head
        pointer = dummy.next
        while first:
            if first.random is not None:
                pointer.random = copies[first.random]
            first = first.next
            pointer = pointer.next
        return dummy.next
            





        