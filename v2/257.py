


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 4 star, dfs
        if not root:
            return []
        rs = []
        self.dfs(root, [], rs)
        return rs

    def dfs(self, node, path, rs):
        if not node.left and not node.right:
            path.append(str(node.val))
            path = "->".join(path)
            rs.append(path)
            return
        if node.left:
            self.dfs(node.left, path + [str(node.val)], rs)   #注意这里参数赋值的位置
        if node.right:
            self.dfs(node.right, path + [str(node.val)], rs)

# a = TreeNode(1)
# a.left = TreeNode(2)
# a.right = TreeNode(3)
# a.left.left = TreeNode(4)
# print(Solution().binaryTreePaths(a))