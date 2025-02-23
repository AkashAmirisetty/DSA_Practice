# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head -> 3 -> 4 -> 5, k = 2
# Output: head -> 3 -> 5
# Explanation: The 2nd node with value 4 was removed.

class Solution:
    def deleteKthNode(self, head, k):
        if head==None:
            return None
        if k==1:
            return head.next
        curr=head
        prev=None
        count=1
        while curr is not None:
            if count==k:
                prev.next=curr.next #when a middle element is deleted this line makes prev element pointing to the curr.next element
                break
            prev=curr
            curr=curr.next
            count+=1
        return head


            
        