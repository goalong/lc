#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (43.31%)
# Total Accepted:    122.3K
# Total Submissions: 282.5K
# Testcase Example:  '[]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree. 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):  # 5 star, no idea, need to master bst feature
        """
        :type root: TreeNode
        """
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False
        

    def next(self):
        """
        :rtype: int
        """
        current = self.stack.pop()
        node = current.right
        while node:
            self.stack.append(node)
            node = node.left
        return current.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

