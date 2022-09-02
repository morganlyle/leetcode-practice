class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        small = prices[0]
        
        for price in prices:
            if price < small:
                small = price
            else:
                if price - small > result:
                    result = price - small
        return result
                