




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 6 star, 没有完全理解
        if not nums:
            return None
        length = len(nums)
        root = TreeNode(nums[length/2])
        left = self.sortedArrayToBST(nums[:length/2])
        right = self.sortedArrayToBST(nums[length/2+1:])
        root.left, root.right = left, right
        return root
