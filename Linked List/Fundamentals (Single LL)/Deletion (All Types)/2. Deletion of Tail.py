# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Input: head -> 1 -> 2 -> 3
# Output: head -> 1 -> 2
# Explanation: The last node was removed.

class Solution:
    def deleteTail(self, head):
        if head==None or head.next==None:
            return None
        curr=head
        while curr.next.next is not None:
            curr=curr.next
        curr.next=None
        return head

        
        

        