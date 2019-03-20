from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 4 star, 没做出来，其实就是需要一个特定的排序，自定义一个比较函数, 这个比较函数构造的比较巧妙
        sorted_nums = sorted([str(i) for i in nums], key=cmp_to_key(self.cmp))
        rs = "".join(sorted_nums).lstrip("0")  # 将"000"之类的转为"0"
        return rs or "0"

    def cmp(self, a, b):
        return int(b + a) - int(a + b)

