# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteKthElement(self, head, k):
        if head==None:
            return None
        if k==1:
            head=head.next
            if head:
                head.prev=None
            return head
        count=1
        prev=None
        curr=head
        while curr.next is not None and count<k:
            prev=curr
            curr=curr.next
            count+=1
        if curr is None:
            return head
        prev.next=curr.next
        if curr.next:
            curr.next.prev=prev
        return head

            