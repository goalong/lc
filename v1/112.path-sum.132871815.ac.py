#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (34.73%)
# Total Accepted:    205K
# Total Submissions: 590.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 5 star.
        if not root:
            return False
        rs = self.dfs(root.val, root, sum)
        return True if rs else False
    
    def dfs(self, cur_sum, node, sum):
        if cur_sum == sum and node.left is None and node.right is None:
            return True
        if node:
            left = right = None
            if node.left:
                left = self.dfs(cur_sum + node.left.val, node.left, sum)
            if node.right:
                right = self.dfs(cur_sum + node.right.val, node.right, sum)
            if left or right:
                return True
