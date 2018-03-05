#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (37.59%)
# Total Accepted:    131K
# Total Submissions: 348.4K
# Testcase Example:  '[]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 
# 
# 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# 
# Return the sum = 12 + 13 = 25.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 5 star.
        if not root:
            return 0
        rs = []
        self.dfs(root, '', rs)
        return sum([int(i) for i in rs])
    
    def dfs(self, node, path, rs):
        if not node.left and not node.right:
            rs.append(path+str(node.val))
            return
        if node.left:
            self.dfs(node.left, path + str(node.val), rs)
        if node.right:
            self.dfs(node.right, path+str(node.val), rs)
        
