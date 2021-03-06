




class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 5 star, 每一层第i个位置的等于上一层i-1和i位置的和
        if numRows == 0:
            return []
        rs = [[0]*(i+1) for i in range(numRows)]
        rs[0] = [1]
        level = 1
        while level < numRows:
            prev_level = rs[level-1]
            cur_level = rs[level]
            for i in range(level+1):
                a, b = 0, 0
                if i-1 >= 0:
                    a = prev_level[i-1]
                if i < level:
                    b = prev_level[i]
                cur_level[i] = a + b
            level += 1
        return rs
# print(Solution().generate(5))