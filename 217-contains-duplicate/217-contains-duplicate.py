class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        i = set()
        
        for n in nums:
            if n in i:
                return True
            i.add(n)
        return False