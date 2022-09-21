class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(set(nums))
        count = 0
        max_count = 0
        previous = 0
        
        for num in nums:
            if count == 0:
                count += 1
                prev = num
            elif num == prev + 1:
                count += 1
                prev = num
            else:
                if count > max_count:
                    max_count = 0
                    max_count += count
                count = 1
                prev = num
        if count > max_count:
            return count
        return max_count