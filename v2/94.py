




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 3 star
        # todo, 非递归写法
        rs = []
        self.inorder(root, rs)
        return rs
    def inorder(self, node, rs):
        if node:
            self.inorder(node.left, rs)
            rs.append(node.val)
            self.inorder(node.right, rs)
