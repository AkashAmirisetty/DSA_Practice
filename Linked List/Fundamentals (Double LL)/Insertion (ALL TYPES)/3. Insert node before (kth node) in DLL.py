# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeKthPosition(self, head, X, K):
        new= ListNode(X,head,None)
        if K==1:
            head.prev=new
            return new
        count=1
        curr=head
        prev=None
        while curr.next is not None and count<K:
            prev=curr
            curr=curr.next
            count+=1
        if count==K:
            new=ListNode(X,curr,prev)
            prev.next=new
            curr.prev=new
        return head
        

            