# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtKthPosition(self, head, X, K):
        new_node=ListNode(X)
        if head==None:
            if K==1:
                return new_node
            else:
                return head
        if K==1:
            return ListNode(X, head) #To insert at first position
        curr=head
        count=1
        while curr is not None and count<K-1:
            curr=curr.next
            count+=1
        new_node.next=curr.next 
        curr.next=new_node
        return head




                



        

        
