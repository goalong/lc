#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (33.52%)
# Total Accepted:    204.8K
# Total Submissions: 611K
# Testcase Example:  '[]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 6 star,  几个分类讨论的情形比较微妙
        if not root:
            return 0
        return self.depth(root)

    def depth(self, node):
        if not node.left and not node.right:
            return 1
        elif node.left and node.right:
            return min(self.depth(node.left), self.depth(node.right)) + 1
        if not node.left and node.right:
            return self.depth(node.right) + 1
        else:
            return self.depth(node.left) + 1
        
