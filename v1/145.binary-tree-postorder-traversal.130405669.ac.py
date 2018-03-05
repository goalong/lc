#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (41.73%)
# Total Accepted:    170K
# Total Submissions: 407.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# For example:
# Given binary tree [1,null,2,3],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 
# 
# 
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
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

