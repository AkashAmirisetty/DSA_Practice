# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(-1)
        carry=0
        curr=dummy
        while l1 or l2 or carry:
            summ=carry
            if l1 is not None:
                summ=summ+l1.val
                l1=l1.next
            if l2 is not None:
                summ=summ+l2.val
                l2=l2.next
            curr.next=ListNode(summ%10)
            carry=summ//10
            curr=curr.next
        return dummy.next



        
                

        
