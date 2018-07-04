


# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         """
#         :type nums: List[int]
#         :type k: int
#         :type t: int
#         :rtype: bool
#         """
#         # 6 star, 有左右两个节点，右节点从第二个到最后一个，左节点则是右节点往左k个之间的范围
#         # 超时了
#         length = len(nums)
#         right = 1
#         while right < length:
#             for left in range(max(0, right-k), right):
#                 if abs(nums[left] - nums[right]) <= t:
#                     return True
#             right += 1
#         return False



class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 6 star, 有左右两个节点，右节点从第二个到最后一个，左节点则是右节点往左k个之间的范围
        if t==0 and len(nums)== len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                if j>=len(nums):
                    break
                if abs(nums[i]-nums[j])<=t:
                    return True
        return False
