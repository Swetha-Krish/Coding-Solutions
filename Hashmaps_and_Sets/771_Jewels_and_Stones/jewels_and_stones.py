class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        out = 0            
        s = set(jewels)
        out = 0

        for stone in stones: 
            if stone in s: 
                out += 1
        
        return out
    
#Time Complexity: O(n + m)
#space Complexity: O(n)