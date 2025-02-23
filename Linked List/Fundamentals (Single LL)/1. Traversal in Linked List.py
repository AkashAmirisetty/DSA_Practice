# # Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def LLTraversal(self, head):
        current=head
        lis=[]
        while current!=None:
            lis.append(current)
            current=current.next
        return lis