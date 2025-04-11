from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        counter = defaultdict(int)

        for c in magazine: 
            counter[c] += 1

        for c in ransomNote: 
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else: 
                counter[c] -= 1
        return True 
    
    
        #Time Complexity: O(m + n)
        #Space Complexity: O(1)