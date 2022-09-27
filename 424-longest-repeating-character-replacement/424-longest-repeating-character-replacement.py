class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        maxf = 0
        result = 0
        
        for r in range(len(s)):
            
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            while (r - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, r - left + 1)
        
        return result 