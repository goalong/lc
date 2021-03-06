



class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 6 star, 动态规划，必须掌握
        # dp[i]表示s[:i]字符串是否能拆分成符合要求的字符串，如果存在s[j:i]是在字符列表里以及dp[j]为真，则dp[i]为真
        str_set = set(wordDict)
        length = len(s)
        dp = [False for _ in range(length+1)]
        dp[0] = 1
        for i in range(1, length+1):
            for j in range(i):
                if dp[j] and s[j:i] in str_set:
                    dp[i] = True
        return dp[-1]
