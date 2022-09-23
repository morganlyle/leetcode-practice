class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        result = int(''.join([bin(x+1)[2:] for x in range(n)]), 2)
        if result > 100000:
            return result % 1000000007
        return result