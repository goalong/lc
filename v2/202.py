

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1 star
        result_set = set()
        while True:
            result = self.gen_result(n)
            if result == 1:
                return True
            if result in result_set:
                return False
            result_set.add(result)
            n = result


    def gen_result(self, x):
        return sum([int(i)**2 for i in str(x)])

print(Solution().gen_result(103))
