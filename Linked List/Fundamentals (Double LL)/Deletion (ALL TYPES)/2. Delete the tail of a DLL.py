# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteTail(self, head):
        if head is None:
            return None
        if head.next is None:
            return None
        curr=head
        while curr.next is not None:
            prev=curr
            curr=curr.next
        prev.next=None
        curr.prev=None
        return head
