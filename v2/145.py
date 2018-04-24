



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
