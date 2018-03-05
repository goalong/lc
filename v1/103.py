# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):  # failed
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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