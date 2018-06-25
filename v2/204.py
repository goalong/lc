


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 6 star, 用一个列表记录每个索引是不是素数，从2开始到根号n, 将这些数的所有倍数全部排除，剩下的就是素数了
        if n < 3:
            return 0
        is_prime = [1] * n
        is_prime[:2] = [0, 0]
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(2*i, n, i):
                    is_prime[j] = 0
        return sum(is_prime)