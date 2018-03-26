#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (32.11%)
# Total Accepted:    97.9K
# Total Submissions: 304.9K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1...n.
# 
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def dfs(self, start, end):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 6 star, 没有理解
        if start > end: return [None]
        res = []
        for rootval in range(start, end+1): #rootval为根节点的值，从start遍历到end
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree: #i遍历符合条件的左子树
                for j in RightTree: #j遍历符合条件的右子树
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        return self.dfs(1, n)
