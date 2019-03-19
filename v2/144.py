


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 4 star, 必须熟练
        rs = []
        self.preorder(root, rs)
        return rs
    def preorder(self, node, rs):
        if node:
            rs.append(node.val)
            self.preorder(node.left, rs)
            self.preorder(node.right, rs)




class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 6 star, 递归版很简单，迭代版没写出来
        # 使用栈，先入右子树，再入左子树，迭代时后入先出，因此会先迭代左子树
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ret





