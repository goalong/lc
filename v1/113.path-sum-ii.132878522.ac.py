#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (35.33%)
# Total Accepted:    156.8K
# Total Submissions: 443.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 
# return
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 5 star.
        if not root:
            return []
        rs = []
        self.dfs([root.val], root.val, root, sum, rs)
        return rs

    def dfs(self, path, cur_sum, node, sum, rs):
        if node.left is None and node.right is None and cur_sum == sum:
            rs.append(path)
            return
        if node.left:
            self.dfs(path + [node.left.val], cur_sum + node.left.val, node.left, sum, rs)
        if node.right:
            self.dfs(path + [node.right.val], cur_sum + node.right.val, node.right, sum, rs)

