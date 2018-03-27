





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 6 star, dfs
        if not root:
            return []
        rs = []
        self.dfs(sum-root.val, root, [root.val], rs)
        return rs

    def dfs(self, gap, node, path, rs):
        if not node.left and not node.right and gap == 0:
            rs.append(path)
            return
        if node:
            if node.left:
                self.dfs(gap-node.left.val, node.left, path + [node.left.val], rs)
            if node.right:
                self.dfs(gap-node.right.val, node.right, path + [node.right.val], rs)
