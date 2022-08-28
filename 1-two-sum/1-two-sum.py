class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dic = {}
        
        for i, n in enumerate(nums):
            result = target - n
            if result in new_dic:
                return [new_dic[result], i]
            new_dic[n] = i