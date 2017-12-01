# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root): # recursvie method is easy, master iterative method
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rs = []
        self._postorder(root, rs)
        return rs
    
    def _postorder(self, node, rs):
        if node:
            self._postorder(node.left, rs)
            self._postorder(node.right, rs)
            rs.append(node.val)
