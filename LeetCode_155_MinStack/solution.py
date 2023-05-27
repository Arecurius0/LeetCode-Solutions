class MinStack(object):

    def __init__(self):
        self.l = []
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.l.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            minV = self.minStack[-1]
            if val < minV:
                self.minStack.append(val)
            else:
                self.minStack.append(minV)
          
    def pop(self):
        """
        :rtype: None
        """
        self.minStack.pop()
        return self.l.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()