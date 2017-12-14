class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):      # 4 stars, no idea, use dp.
        if s=="" or s[0]=='0': return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
        	before = int(s[i-2:i])
        	if 10 < before < 20 or 26 >= before > 20:
        		dp[i] = dp[i-1] + dp[i-2] 
        	elif before in (10, 20):
        		dp[i] = dp[i-2]
        	elif 9 >= int(s[i-1]) >= 1:
        		dp[i] = dp[i-1]
        return dp[-1]

 

    # def numDecodings(self, s):
    #     n = len(s)
    #     if not n:
    #         return 0

    #     dp = [0] * (n + 1)

    #     dp[0] = 1
    #     dp[1] = int(s[0] != '0')

    #     for i in range(2, n + 1):
    #         two, one = int(s[i-2 : i]), int(s[i-1])
    #         if 10 <= two <= 26:
    #             dp[i] = (dp[i-1] + dp[i-2]) if one else dp[i-2]
    #         elif 1 <= one <= 9:
    #             dp[i] = dp[i-1]

    #     return dp[-1]


# 虽然通过了，但是不能理解为什么'1100'的结果是0，我以为是2呢  todo 

s = Solution()
print(s.numDecodings(
    '11000'))