




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 6 star, 多加练习
        # 构造一个height函数，计算每个节点的高度，然后递归比较左右子树的高度
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1
