




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 6 star, 多练习
        import sys
        return self.is_valid(-sys.maxsize, sys.maxsize, root)

    def is_valid(self, min, max, node):
        # 注意引入了上限和下限两个变量来比较
        if not node:
            return True
        if node.val <= min or node.val >= max:
            return False
        return self.is_valid(min, node.val, node.left) and self.is_valid(node.val, max, node.right)

