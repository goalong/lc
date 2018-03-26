




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 6 star, 必须掌握
        return self.helper(root, root)
    def helper(self, node1, node2):
        if not node1 and not node2:  # 都是None
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)