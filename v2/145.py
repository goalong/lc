



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 4 star, 熟练递归及迭代实现
        # todo, 迭代的实现
        rs = []
        self.postorder(root, rs)
        return rs

    def postorder(self, node, rs):
        if node:
            self.postorder(node.left, rs)
            self.postorder(node.right, rs)
            rs.append(node.val)


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 7 star, 非递归版本，必须掌握，面试遇到过
        # 后续遍历是先遍历左子树，后遍历右子树，最后才是根节点
        # 仍然使用栈，先将根节点入栈，然后入栈左子树和右子树，因为后进先出，所以实际顺序是右子树、左子树、根节点，最后将结果翻转即可
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return ret[::-1]


