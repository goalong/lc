#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (41.01%)
# Total Accepted:    138.2K
# Total Submissions: 337K
# Testcase Example:  '4\n2'
#
# 
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# 
# 
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#
class Solution:
    # 6 star. 换成python3终于ac了，python2下还是tle.
    def combine(self, n, k):
        def dfs(start, count, path):
            if count == k:
                ret.append(path)
                return
            for i in range(start, n + 1):
                if count + 1 > k:
                    return
                dfs(i + 1, count+1, path + [i])
        ret = []
        dfs(1, 0, [])
        return ret
