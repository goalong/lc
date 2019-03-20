# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 3 star, pass，已掌握
        # 按层次遍历，将每一层的节点放入一个列表，列表最后的元素的值就是该层从右边看到的值，然后遍历该列表，取它们的左右子树放到下一层的列表，接着进行下一层列表的遍历
        if not root:
            return []
        queue = [root]
        next_level = []
        ret = []
        while queue:
            ret.append(queue[-1].val)
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            next_level = []
        return ret
