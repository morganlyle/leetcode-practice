class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        x = len(nums)
        
        prod = 1
        
        for i in range(1, x):
            prod = prod*nums[i - 1]
            result[i] *= prod
        prod = 1
        
        for i in range(x-2, -1, -1):
            prod = prod*nums[i+1]
            result[i]*= prod
            
        return result
            