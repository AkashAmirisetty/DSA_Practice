# Definition for Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
    # -----------------MY APPROACH----------------------------------
        # length=0
        # curr=head
        # while curr is not None:
        #     length+=1
        #     curr=curr.next
        # nodetoberemoved=length-n
        # if nodetoberemoved==0:
        #     return head.next
        # curr=head
        # for i in range(nodetoberemoved-1):
        #     curr=curr.next
        # curr.next=curr.next.next
        # return head
        
    # ---------------Optimal Solution(STRIVER)-----------------------
        fast=head
        for i in range(0,n): #first traverse the fast to n(0,1,2...n)
            fast=fast.next
        slow=head
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        if fast is None: #This is the case when number of elements is equal to n
            return head.next
        slow.next=slow.next.next #because the slow points to the before node to the node to be deleted
        return head





        