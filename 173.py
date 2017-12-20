# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):  # 5 star, no idea, need to master bst feature
        """
        :type root: TreeNode
        """
        self.stack = []
        node = self.root
        while node:
            self.stack.append(node)
            node = node.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False
        

    def next(self):
        """
        :rtype: int
        """
        current = self.stack.pop()
        node = current.right
        while node:
            self.stack.append(node)
            node = node.left
        return current.val


作者：Jason_Yuan
链接：http://www.jianshu.com/p/68e1b84d40e2
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
