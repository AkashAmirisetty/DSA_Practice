# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeGivenNode(self, node, X):
        prev = node.prev
        new=ListNode(X, node,prev)
        prev.next=new
        node.prev=new
        return 
        

        
