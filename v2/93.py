




class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 6 star, dfs
        # IP地址由四部分，每部分由1到3位的数字组成，每个数字小于等于255
        rs = []
        self.dfs(s, 0, rs, [])
        return rs

    def dfs(self, s, parts, rs, path):
        if parts == 4:
            if s == "":
                rs.append(".".join(path))
            else:
                return
        for i in range(1, 4):
            if i <= len(s) and int(s[:i]) <= 255:
                if i > 1 and s[0] == "0":  # 除了0以外不能有03这种以0开头的
                    break
                self.dfs(s[i:], parts+1, rs, path+[s[:i]])


# print(Solution().restoreIpAddresses("00100"))