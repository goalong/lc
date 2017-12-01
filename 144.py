# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rs = []
        self._preorder(root, rs)
        return rs
    
    def _preorder(self, node, rs):
        if node:
            rs.append(node.val)
            self._preorder(node.left, rs)
            self._preorder(node.right, rs)