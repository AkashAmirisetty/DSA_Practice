# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # -----------My approach-------------------

        # if head is None or head.next is None:
        #     return head
        # zero_head=zero_tail=ListNode(-1)
        # one_head=one_tail=ListNode(-1)
        # two_head=two_tail=ListNode(-1)
        # curr=head
        # while curr is not None:
        #     if curr.val==0:
        #         zero_tail.next=curr
        #         zero_tail=zero_tail.next
        #     elif curr.val==1:
        #         one_tail.next=curr
        #         one_tail=one_tail.next
        #     elif curr.val==2:
        #         two_tail.next=curr
        #         two_tail=two_tail.next
        #     curr=curr.next
            
        # zero_tail.next = one_head.next if one_head.next else two_head.next
        # one_tail.next = two_head.next
        # two_tail.next = None
        # return zero_head.next if zero_head.next else one_head.next

        #----------------- Brute-Force  T.C:O(2N), SC: O(1)------------------------------

        # if head is None or head.next is None:
        #     return head
        # curr=head
        # cnt0=0
        # cnt1=0
        # cnt2=0
        # while curr is not None:
        #     if curr.val==0:
        #         cnt0+=1
        #     elif curr.val==1:
        #         cnt1+=1
        #     else:
        #         cnt2+=1
        #     curr=curr.next
        # curr=head
        # while curr is not None:
        #     if cnt0!=0:
        #         curr.val=0
        #         cnt0-=1
        #     elif cnt1!=0:
        #         curr.val=1
        #         cnt1-=1
        #     elif cnt2!=0:
        #         curr.val=2
        #         cnt2-=1
        #     curr=curr.next
        # return head

        #------------  Optimal Solution------------------------
        if head is None or head.next is None:
            return head
        curr=head
        zeroHead=ListNode(-1)
        oneHead=ListNode(-1)
        twoHead=ListNode(-1)
        zero= zeroHead
        one=oneHead
        two=twoHead
        while curr is not None:
            if curr.val==0:
                zero.next=curr
                zero=curr
            elif curr.val==1:
                one.next=curr
                one=curr
            elif curr.val==2:
                two.next=curr
                two=curr
            curr=curr.next
        zero.next=oneHead.next if oneHead.next is not None else twoHead.next
        one.next=twoHead.next
        two.next=None
        return zeroHead.next















