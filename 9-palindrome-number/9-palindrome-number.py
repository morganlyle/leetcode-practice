class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """     
        if x < 0:
            return False
        
        i = 0
        new = x
        
        while new != 0:
            i = i*10 + new%10
            new = new/10
        if i == x:
            return True
        