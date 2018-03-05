class Solution(object):
    def lengthOfLongestSubstring(self, s):  # 
        """
        :type s: str
        :rtype: int
        """
        max_len, start = 0, 0
        memo = {}
        for i, char in enumerate(s):
            if char not in memo or memo[char] < start:
                max_len = max(max_len, i + 1 - start)
            else:
                start = memo[char] + 1    
            memo[char] = i
        return max_len
