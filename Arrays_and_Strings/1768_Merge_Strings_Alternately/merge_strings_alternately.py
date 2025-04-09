class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a = 0 ; b = 0
        s = [] 

        while a<len(word1) and b<len(word2): 
            s.append(word1[a])
            s.append(word2[b])
            a += 1
            b += 1

        while a<len(word1): 
            s.append(word1[a])
            a += 1

        while b<len(word2): 
            s.append(word2[b])
            b += 1

        return(''.join(s))
            

        # Time complexity: O(A + B)
        # Space Complexity: O(A + B)