# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head -> 3 -> 4 -> 5, X = 5
# Output: head -> 3 -> 4
# Explanation: The node with value 5 was removed.


class Solution:
    def deleteNodeWithValueX(self, head, X):
        if head==None:
            return None
        if head.val==X:
            return head.next
        curr=head
        prev=None
        while curr is not None:
            if curr.val==X:
                prev.next=curr.next
                break
            prev=curr
            curr=curr.next
        return head


        
