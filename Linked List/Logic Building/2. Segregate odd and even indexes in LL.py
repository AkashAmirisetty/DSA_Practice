# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        arr=[]
        curr=head
        # for odd indexes
        while curr is not None and curr.next is not None:
            arr.append(curr.val)
            curr=curr.next.next
        if curr is not None:
            arr.append(curr.val)
        # for even indexes
        curr=head.next
        while curr is not None and curr.next is not None:
            arr.append(curr.val)
            curr=curr.next.next
        if curr is not None:
            arr.append(curr.val)
        curr=head
        i=0
        while curr is not None:
            curr.val=arr[i]
            curr=curr.next
            i+=1
        return head




            

        


        
        


            
        