# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
# ----------------------My Approach-------------------------------------

        num_str=""
        curr=head
        while curr is not None:
            num_str+=str(curr.val)
            curr=curr.next
        n=len(num_str)
        left=0
        right=n-1
        while left<right:
            if num_str[left]!=num_str[right]:
                return False
            left+=1
            right-=1
        return True





            