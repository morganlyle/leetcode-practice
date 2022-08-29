class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        x = [amount + 1] * (amount + 1)
        x[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    x[i] = min(x[i], 1 + x[i - c])
        return x[amount] if x[amount] != amount + 1 else -1