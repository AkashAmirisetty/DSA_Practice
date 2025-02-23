# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head -> 1 -> 2 -> 3
# Output: head -> 2 -> 3
# Explanation: The first node was removed.


class Solution:
    def deleteHead(self, head):
        curr=head
        if curr==None:
            return None
        head=curr.next
        del curr
        return head

        
        