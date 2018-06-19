


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.in_order(root)


    def next(self):
        if self.stack:
            return self.stack.pop()

    def hasNext(self):
        return len(self.stack) > 0

    def in_order(self, node):
        if node:
            self.in_order(node.right)
            self.stack.append(node.val)
            self.in_order(node.left)


