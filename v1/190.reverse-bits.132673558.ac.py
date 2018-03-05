#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (29.40%)
# Total Accepted:    127.5K
# Total Submissions: 433.6K
# Testcase Example:  '           0 (00000000000000000000000000000000)'
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as
# 00000010100101000001111010011100), return 964176192 (represented in binary as
# 00111001011110000010100101000000).
# 
# 
# Follow up:
# If this function is called many times, how would you optimize it?
# 
# 
# Related problem: Reverse Integer
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 3 star, my solution is too stupid.
        rs = ['0'] * 32
        _n = list(bin(n)[2:][::-1])
        rs[:len(_n)] = _n
        return int("".join(rs), 2)
        
        
