# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rs = []
        self._inorder(root, rs)
        return rs

    def _inorder(self, node, rs):
        if node:
            self._inorder(node.left, rs)
            rs.append(node.val)
            self._inorder(node.right, rs)