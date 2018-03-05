#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (28.31%)
# Total Accepted:    100K
# Total Submissions: 353.3K
# Testcase Example:  '"0000"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# 
# For example:
# Given "25525511135",
# 
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# 
#
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 6 star, didn't come out.
        rs = []
        self.dfs(0, [], s, rs)
        return rs

    def dfs(self, parts, path, s, rs):
        if parts == 4:
            if s == "":
                rs.append(".".join(path))
            else:
                return
        for i in range(1, 4):
            if i <= len(s) and int(s[:i]) <= 255:
                self.dfs(parts+1, path+[s[:i]], s[i:], rs)
            if s and s[0] == '0':
                break
