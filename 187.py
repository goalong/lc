class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 1 star.
        n = len(s)
        if n <= 10:
        	return []
        str_map = {}
        for i in range(n-10+2):
        	seq = s[i:i+10]
        	if seq in str_map:
        		str_map[seq] += 1
        	else:
        		str_map[seq] = 1
        return [i for i in str_map.keys() if str_map[i] > 1]


print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))