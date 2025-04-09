class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    """
        closest = nums[0]
        
        for x in nums:
            if abs(x)< abs(closest): closest = x
        
        if closest < 0 and abs(closest) in nums: return abs(closest)
        else: return closest


        # Time complexity: O(n)
        # Space Complexity: O(1)


