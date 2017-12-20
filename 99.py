class Solution(object):
    def recoverTree(self, root):    # 4 star.
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
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