# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addOne(self, head):

        # ---------------My Approach-------------------
        num_str=""
        curr=head
        while curr is not None:
            num_str+=str(curr.val)
            curr=curr.next
        num_str=int(num_str)
        num_str=num_str+1
        num_str=str(num_str)
        dummy=ListNode(-1)
        curr=dummy
        for digit in num_str:
            curr.next=ListNode(int(digit))
            curr=curr.next
        return dummy.next

        




