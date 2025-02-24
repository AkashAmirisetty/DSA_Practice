# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtTail(self, head, X):
        new_node=ListNode(X)
        if head==None:
            return new_node
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        return head

        

