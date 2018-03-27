




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
        # 6 star, 没理解，需多看
        # 先序遍历的非递归实现
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

