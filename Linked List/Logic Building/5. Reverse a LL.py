# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        stack=[]
        curr=head
        while curr is not None:
            stack.append(curr)
            curr=curr.next
        dummy=ListNode(-1)
        curr=dummy
        while stack:
            node=stack.pop()
            curr.next=node
            curr=curr.next
            
        curr.next=None
        return dummy.next





