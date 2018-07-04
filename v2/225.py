
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 5 star, 一个队列专门用来入栈，出栈时将其倒入另一个队列直到最后一个
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
            cur = self.queue_a.pop(0)
            if self.queue_a:
                self.queue_b.append(cur)
            else:
                self.queue_a, self.queue_b = self.queue_b, self.queue_a
                return cur


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.queue_a:
            cur = self.queue_a.pop(0)
            self.queue_b.append(cur)
            if not self.queue_a:
                self.queue_a, self.queue_b = self.queue_b, self.queue_a
                return cur


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue_a

