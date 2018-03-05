#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (29.98%)
# Total Accepted:    152.3K
# Total Submissions: 508.2K
# Testcase Example:  '[1,2]\nnode with value 1\nnode with value 2'
#
# 
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# 
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# 
# ⁠       _______3______
# ⁠      /              \
# ⁠   ___5__          ___1__
# ⁠  /      \        /      \
# ⁠  6      _2       0       8
# ⁠        /  \
# ⁠        7   4
# 
# 
# 
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another
# example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of
# itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 6 star. no idea.
        if not root:
            return root
        if root in (p, q):
            return root
        left, right = (self.lowestCommonAncestor(k, p, q) for k in (root.left, root.right))
        if left and right:
            return root
        return left or right
