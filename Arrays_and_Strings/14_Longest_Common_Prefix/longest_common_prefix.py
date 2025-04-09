class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = float('inf')
        i = 0

        for s in strs:
            if len(s)< min_len:
                min_len = len(s)
                
        while i in range(min_len):
            for s in strs:
                if s[i]!= strs[0][i]:
                    return s[:i]  
            i += 1
            
        return s[:i]
    
# Time complexity: O(n * m)
# Space Complexity: O(1)