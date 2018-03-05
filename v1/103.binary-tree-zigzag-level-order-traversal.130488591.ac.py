#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (36.46%)
# Total Accepted:    129.8K
# Total Submissions: 356.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        rs = [[root.val]]
        children = []
        index = 1
        while queue:
            for node in queue:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if not children:
                break
            if index % 2 == 1:
                level_data = [node.val for node in children[::-1]]
            else:
                level_data = [node.val for node in children]
            rs.append(level_data)
            queue = children
            children = []
            index += 1
        return rs

# a = TreeNode(3)
# b = TreeNode(9)
# c = TreeNode(20)
# d = TreeNode(15)
# e = TreeNode(7)

# c.left = d
# c.right = e
# a.left, a.right = b, c

# print(Solution().zigzagLevelOrder(a))
