




class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 6 star, 二分法
        low, high = 0, x
        while low <= high:
            middle = (low+high)//2
            _pow = middle * middle
            if _pow <= x and (middle+1)*(middle+1)>x:
                return middle
            elif _pow > x:
                high = middle - 1
            else:
                low = middle + 1
