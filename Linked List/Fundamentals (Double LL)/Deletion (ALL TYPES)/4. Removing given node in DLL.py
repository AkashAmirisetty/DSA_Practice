# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteGivenNode(self, node):
        front=node.next
        prev=node.prev
        if front is None: #Edge case if the node to be removed is before null
            prev.next=None
            node.prev=None
            return
        prev.next=front
        front.prev=prev
        node.next=None
        node.prev=None
        
