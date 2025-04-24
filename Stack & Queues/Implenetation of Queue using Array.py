class ArrayQueue:
    def __init__(self):
        self.size=1000
        self.queue=[0]*self.size
        self.currsize=0
        self.start=-1
        self.end=-1

    def push(self, x):
        if self.currsize==self.size:
            # return ("Overflow")
            return None
        if self.currsize==0:
            self.start,self.end=0,0
        else:
            self.end=(self.end+1)%self.size
        self.queue[self.end]=x
        self.currsize+=1
        
    def pop(self):
        if self.currsize==0:
            # return ("Empty")
            return None
        cl=self.queue[self.start]
        if self.currsize==1:
            self.start=-1
            self.end=-1
        else:
            self.start=(self.start+1)%self.size
        self.currsize-=1
        return cl

    def peek(self):
        if self.currsize==0:
            return None
        return self.queue[self.start]

    def isEmpty(self):
        if self.currsize==0:
            return True 
        else:
            return False  
