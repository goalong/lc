


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