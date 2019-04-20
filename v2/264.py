


# class Solution(object):
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # 4 star
#         # todo, 超时了
#         count = 1
#         num = 1
#         while count < n:
#             num += 1
#             if self.is_ugly(num):
#                 count += 1
#         return num
#
#     def is_ugly(self, num):
#         for i in (2, 3, 5):
#             while num % i == 0:
#                 num = num // i
#         return num == 1

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 6 star, 很巧妙的解法，多练几遍
        a, b, c = 0, 0, 0
        result = [1 for _ in range(n)]
        for i in range(1, n):
            result[i] = min(result[a]*2, result[b]*3, result[c]*5)
            if result[i] == result[a]*2:
                a += 1
            if result[i] == result[b]*3:
                b += 1
            if result[i] == result[c] * 5:
                c += 1
        return result[n-1]

print(Solution().nthUglyNumber(10))