class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums): # 3 star, 重点是这个比较函数
        def compare(a, b):
            return int(b+a) - int(a+b)
        nums = sorted([str(i) for i in nums], cmp=compare)
        ans = ''.join(nums).lstrip('0')
        return ans or "0"
        