class ArrayStack:
    def __init__(self):
        self.size = 1000
        self.stack = [0] * self.size
        self.top_ind = -1  

    def push(self, x):
        if self.top_ind >= self.size - 1:
            return  # overflow condition
        self.top_ind += 1
        self.stack[self.top_ind] = x

    def pop(self):
        if self.top_ind == -1:
            return -1  # When the stack is empty
        popped = self.stack[self.top_ind]
        self.top_ind -= 1
        return popped

    def top(self):  
        if self.top_ind == -1:
            return 
        return self.stack[self.top_ind]

    def isEmpty(self):
        return self.top_ind == -1


