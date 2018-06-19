# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # 5 star, 运用中序遍历的特性，中序遍历二叉搜索树可以以从小到大的顺序访问所有的元素
        self.stack = []
        self.in_order(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()

    def in_order(self, node):
        if node:
            # 对中序排序做了调整，方便后面从小到大取出元素
            self.in_order(node.right)
            self.stack.append(node.val)
            self.in_order(node.left)


            # Your BSTIterator will be called like this:
            # i, v = BSTIterator(root), []
            # while i.hasNext(): v.append(i.next())