#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (36.33%)
# Total Accepted:    157.8K
# Total Submissions: 434.3K
# Testcase Example:  '[]'
#
# 
# Given a binary tree, flatten it to a linked list in-place.
# 
# 
# 
# For example,
# Given
# 
# ⁠        1
# ⁠       / \
# ⁠      2   5
# ⁠     / \   \
# ⁠    3   4   6
# 
# 
# 
# The flattened tree should look like:
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠     \
# ⁠      3
# ⁠       \
# ⁠        4
# ⁠         \
# ⁠          5
# ⁠           \
# ⁠            6
# 
# 
# click to show hints.
# 
# Hints:
# If you notice carefully in the flattened tree, each node's right child points
# to the next node of a pre-order traversal.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 6 star， 先序遍历非递归实现
        if not root:
            return
        stack = [root]
        prev = TreeNode(None)
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            prev.left, prev.right = None, cur
            prev = cur
        

