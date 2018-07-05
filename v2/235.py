


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 6 star, 分别找到两个节点从根节点到其自身的路径，对路径进行对比，最后一个相同的节点即是结果
        # 注意，路径有个特点，有相同祖先的话，则从根节点到该祖先的路径是一样的
        p_path = self.get_path(root, p)
        q_path = self.get_path(root, q)
        index = 0
        min_length = min(len(p_path), len(q_path))
        for i in range(min_length):
            if p_path[i].val == q_path[i].val:
                index = i
                continue
            else:
                break
        return p_path[index]

    def get_path(self, root, node):
        path = [root]
        ptr = root
        while ptr.val != node.val:
            if ptr.val > node.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
            path.append(ptr)
        return path