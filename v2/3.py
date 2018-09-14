


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 5 star, 遍历字符串，使用字典记录每个字母到索引的映射
        # 这个解法有点绕，回头用滑动窗口法重做
        rs, start = 0, 0
        memo = {}
        for index, v in enumerate(s):
            # 当前字母不在s[start:index]范围内，可以继续向前遍历
            if v not in memo or memo[v] < start:
                rs = max(rs, index + 1 - start)
            # 当前字母在s[start:index]有重复，新的起点从重复字母索引的下一位开始
            else:
                start = memo[v] + 1
            memo[v] = index
        return rs
