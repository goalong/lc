





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 5 star, dfs, 注意这里使用了列表类型的参数来记录所有根到叶子组成的数字，因为列表是可变对象
        if not root:
            return 0
        rs = []
        self.dfs(root, str(root.val), rs)
        return sum(rs)

    def dfs(self, node, path, rs):
        if not node.left and not node.right:
            rs.append(int(path))
            return
        if node.left:
            self.dfs(node.left, path + str(node.left.val), rs)
        if node.right:
            self.dfs(node.right, path + str(node.right.val), rs)

# a = TreeNode(9)
# print(Solution().sumNumbers(a))