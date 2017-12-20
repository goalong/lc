class Solution(object):
    

    def restoreIpAddresses(self, s):  # 5 star, no idea, dfs.
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, parts, res, ip):
            if parts == 4:
                if s == '':
                    res.append(ip[1:])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], parts + 1, res, ip + '.' + s[:i])
                        if s[0] == '0':
                            break

        res = []
        dfs(s, 0, res, '')  # parts 初始化为0
        return res


print(Solution().restoreIpAddresses('2552551113'))
