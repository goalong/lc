




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 6 star， no idea, dfs, 必须掌握
        # todo, 必须掌握
        if not root:
            return False
        rs = self.dfs(root.val, root, sum)
        return True if rs else False


    def dfs(self, current, node , sum):
        if current == sum and not node.left and not node.right:
            return True
        if node:
            left = right = None
            if node.left:
                left = self.dfs(current+node.left.val, node.left, sum)
            if node.right:
                right = self.dfs(current+node.right.val, node.right, sum)
            # 左边或者右边的和等于sum了，则True
            if left or right:
                return True