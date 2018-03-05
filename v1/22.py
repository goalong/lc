class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rs = []
        self.helper(n, n, '', rs)
        return rs

    def helper(self, left, right, current, rs):
    	if left == right == 0:
    		rs.append(current)
    		return
    	if left > 0:
    		self.helper(left-1, right, current+'(', rs)
    	if right > left:
    		self.helper(left, right-1, current + ')', rs)
        
