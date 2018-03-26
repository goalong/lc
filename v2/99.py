




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 6 star, 应该有更好的解法
        # 中序遍历会生成一个递增的数组， 用两个列表分别存储中序遍历时的节点和节点的值，对节点的值的列表排序，然后遍历节点的列表，重新赋值
        l, pl = [], []
        self.inorder(root, l, pl)
        l.sort()
        for i in range(len(l)):
            pl[i].val = l[i]


    def inorder(self, node, l, pl):
        if node:
            self.inorder(node.left, l, pl)
            l.append(node.val)
            pl.append(node)
            self.inorder(node.right, l, pl)
