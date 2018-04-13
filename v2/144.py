


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

