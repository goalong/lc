class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        last = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == last:
            self.min_stack.pop()
        return last
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# stack = MinStack()
# stack.push(0)
# stack.push(1)
# stack.push(0)

# print stack.getMin()
# stack.pop()
# print stack.getMin()
