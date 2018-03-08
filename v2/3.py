


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这个解法有点绕，回头用滑动窗口法重做
        rs, start = 0, 0
        memo = {}
        for index, v in enumerate(s):
            if v not in memo or memo[v] < start:
                rs = max(rs, index + 1 - start)
            else:
                start = memo[v] + 1
            memo[v] = index
        return rs
