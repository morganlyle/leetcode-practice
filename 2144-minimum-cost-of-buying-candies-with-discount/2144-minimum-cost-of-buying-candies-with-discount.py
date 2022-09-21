class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        return sum(cost) - sum(sorted(cost)[-3::-3])
        
        