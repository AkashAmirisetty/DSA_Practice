class Node:
    def __init__(self,x):
        self.val=x
        self.next=None
class LinkedListQueue:
    def __init__(self):
        self.size=0
        self.head=None
        self.start=None
        self.end=None

    def push(self, x):
        ele=Node(x)
        if self.start==None:
            self.start=self.end=ele
            
        else:
            self.end.next=ele
            self.end=ele
        self.size+=1

    def pop(self):
        if self.start== None:
            return None
        poped=self.start.val
        temp=self.start
        self.start=self.start.next
        del temp
        self.size-=1
        return poped

    def peek(self):
        if self.start==None:
            return None
        return self.start.val
     
    def isEmpty(self):
        return self.size==0
