# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertBeforeX(self, head, X, val):
        new_node=ListNode(val)
        if head==None:
            return None
        if head.val==X:
           new_node.next=head
           return new_node
        curr=head
        while curr.next is not None:
            if curr.next.val==X:
                new_node.next=curr.next
                curr.next=new_node
                break
            curr=curr.next
        return head
            


            
        
            