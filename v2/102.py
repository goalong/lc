




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 6 star, 类似队列的处理方式，对每一层的放到一个列表里，遍历时将子节点放到新的列表里，然后开始下一层的处理
        if not root:
            return []
        rs = []
        queue = [root]
        while queue:
            current_level = queue
            queue = []
            rs.append([i.val for i in current_level])
            for node in current_level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rs

