




class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 动态规划，6 star, 没有掌握，需多练
        # https://shenjie1993.gitbooks.io/leetcode-python/072%20Edit%20Distance.html
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]