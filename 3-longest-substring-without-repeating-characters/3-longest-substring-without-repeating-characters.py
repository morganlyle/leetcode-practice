class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last = {}
        max_count = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in last:
                start = max(start, last[s[i]] + 1)
            max_count = max(max_count, i - start + 1)
            last[s[i]] = i
        return max_count
        
        
        
        
        