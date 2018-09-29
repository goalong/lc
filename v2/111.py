




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 6 star, 分类讨论的情形比较巧妙，一开始做错了
        # todo, 需要掌握
        if not root:
            return 0
        return self._minDepth(root)

    def _minDepth(self, node):
        if not node.left and not node.right:
            return 1
        elif node.left and node.right:
            return min(self._minDepth(node.left), self._minDepth(node.right)) + 1
        elif node.left:
            return self._minDepth(node.left) + 1
        else:
            return self._minDepth(node.right) + 1