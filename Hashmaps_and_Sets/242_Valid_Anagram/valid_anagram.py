from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False 
        
        S = defaultdict(int)
        T = defaultdict(int)

        for c in s:
            S[c] += 1
        for c in t: 
            T[c] += 1

     
        return S == T
        
        #Time Complexity: O(n)
        #Space Complexity: O(n)