#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (30.86%)
# Total Accepted:    85.4K
# Total Submissions: 276.8K
# Testcase Example:  '[0,1]'
#
# 
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# 
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# constant space solution?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 6 star, 两个列表分别存储每个节点和每个节点的值，依据中序遍历递增的特点，此题等价为一个递增的序列中两个值交换了位置
        l, pl = [], []
        self.inorder(root, l, pl)
        l.sort()
        for i in range(len(l)):
            pl[i].val = l[i]
    
    def inorder(self, node, l, pl):
        if node:
            self.inorder(node.left, l, pl)
            l.append(node.val)
            pl.append(node)
            self.inorder(node.right, l, pl)
