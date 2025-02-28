# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeHead(self, head, X):
        new_node=ListNode(X,head,None)
        head.prev=new_node
        new_node.prev=None
        new_node.next=head
        return new_node
