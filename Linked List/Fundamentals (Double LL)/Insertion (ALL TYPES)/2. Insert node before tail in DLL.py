# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeTail(self, head, X):
        if head.next is None:
            new= ListNode(X,head,None)
            head.prev=new
            return new
        tail=head
        while tail.next is not None:
            tail=tail.next
        previ=tail.prev
        newNode=ListNode(X, tail,previ)
        previ.next=newNode
        tail.prev=newNode
        return head


        
