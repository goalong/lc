class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_a = []
        self.queue_b = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue_a.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.queue_a:
            i = self.queue_a.pop(0)
            if not self.queue_a:
                self.queue_a, self.queue_b = self.queue_b, self.queue_a
                return i
            else:
                self.queue_b.append(i)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.queue_a:
            i = self.queue_a.pop(0)
            if not self.queue_a:
                self.queue_b.append(i)
                self.queue_a, self.queue_b = self.queue_b, self.queue_a
                return i
            else:
                self.queue_b.append(i)

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue_a


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# a = MyStack()
# print a.empty()

# a.push(1)
# a.push(2)

# print a.top()

# a.pop()

# print a.top()
