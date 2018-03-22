




class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 在nums1中从预留的最后一个位置，逐个对比两个数组的末尾的值，并向新的位置填充
        # 4 star
        index = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[index] = nums1[m-1]
                m -= 1
            else:
                nums1[index] = nums2[n-1]
                n -= 1
            index -= 1
        if m <= 0:  # nums1已经全部填充到新的nums1, 剩下的nums2补到nums1的最前面
            nums1[:n] = nums2[:n]
        # print(nums1)

# Solution().merge([0], 0, [1], 1)