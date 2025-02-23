# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtHead(self, head, X):
        curr=ListNode(X)
        curr.next=head
        head=curr
        return head

        
