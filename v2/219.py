


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 4 star, 使用一个字典记录相同值的索引，如果索引之间的差小于等于k, 则返回True
        num_to_index = {}
        for i, num in enumerate(nums):
            if num in num_to_index:
                if i - num_to_index[num][-1] <= k:
                    return True
                num_to_index[num].append(i)
            else:
                num_to_index[num] = [i]
        return False

