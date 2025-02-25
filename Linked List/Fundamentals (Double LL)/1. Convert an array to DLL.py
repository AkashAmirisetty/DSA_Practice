# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def arrayToLinkedList(self, nums):
        if len(nums)==0:
            return None
        head=ListNode(nums[0])
        previous=head
        for i in range(1,len(nums)):
            current=ListNode(nums[i],None,previous)
            previous.next=current
            previous=current #move
        return head


