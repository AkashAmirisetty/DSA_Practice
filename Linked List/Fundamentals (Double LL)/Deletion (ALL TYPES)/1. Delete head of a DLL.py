# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteHead(self, head):
        if head is None:
            return None
        if head.next is None:
            return None
        prev=head
        head=head.next
        head.prev=None
        prev.next=None
        return head
        