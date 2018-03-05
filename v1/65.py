class Solution(object):
    def isNumber(self, s):   # 1 star.
        """
        :type s: str
        :rtype: bool
        """
        try: 
        	float(s)
        	return True
        except:
        	return False
        
