




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 3 star
        # todo, 非递归写法
        rs = []
        self.inorder(root, rs)
        return rs
    def inorder(self, node, rs):
        if node:
            self.inorder(node.left, rs)
            rs.append(node.val)
            self.inorder(node.right, rs)


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 5 star
        # 非递归写法, 先一直往左遍历，并加到栈中，然后到最左子树后，开始出栈，如果有右节点，将右节点入栈
        if not root:
            return []
        stack = []
        rs = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                rs.append(node.val)
                node = node.right
        return rs
