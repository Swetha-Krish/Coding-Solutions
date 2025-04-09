class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        new = []
        while i in range(len(nums)):
            start = nums[i]
            while i<len(nums)-1 and nums[i] +1 == nums[i+1]:
                i+=1 
                
            if start == nums[i]:
                new.append(str(nums[i]))
            else:
                new.append(str(start) + "->" + str(nums[i]))
            
            i+=1
            
        return new
    
# Time complexity: O(n)
# Space Complexity: O(1)