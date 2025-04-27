class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

class LinkedListStack:
    def __init__(self):
        self.size=0
        self.head=None

    def push(self, x):
        ele=Node(x)
        ele.next=self.head
        self.head=ele
        self.size+=1

    def pop(self):
        if self.head is None:
            return -1
        popped=self.head.val
        temp=self.head
        self.head=self.head.next
        del temp
        self.size-=1
        return popped
    def top(self):
        return self.head.val

    def isEmpty(self):
        if self.size ==0:
            return True 
        else:
            return False




