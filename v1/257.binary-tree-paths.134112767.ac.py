#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (40.85%)
# Total Accepted:    149.4K
# Total Submissions: 365.8K
# Testcase Example:  '[1,2,3,null,5]'
#
# 
# Given a binary tree, return all root-to-leaf paths.
# 
# 
# For example, given the following binary tree:
# 
# 
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 
# 
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 4 star.
        if not root:
            return []
        rs = []
        self.dfs(root, [], rs)
        return ["->".join(i) for i in rs]
        

    def dfs(self, node, path, rs):
        if not node.left and not node.right:
            rs.append(path + [str(node.val)])
            return
        if node.left:
            self.dfs(node.left, path + [str(node.val)], rs)
        if node.right:
            self.dfs(node.right, path+[str(node.val)], rs)
        
