
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 6 star, 没有理解
        start = sums = 0
        for x in range(len(gas)):
            sums += gas[x] - cost[x]
            if sums < 0:
                start, sums = x + 1, 0
        return start if sum(gas) >= sum(cost) else -1

print(Solution().canCompleteCircuit([1,2,3,4,5],
[3,4,5,1,2]))

