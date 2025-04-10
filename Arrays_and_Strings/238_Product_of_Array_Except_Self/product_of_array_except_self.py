class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l_mult = 1
        r_mult = 1
        n =len(nums)
        left = [0] * n
        right = [0] * n
        arr = [0] * n
        r = 0 
        
        for i in range(n):
            j = -i-1
            left[i] = l_mult
            right[j] = r_mult 
            l_mult *= nums[i] 
            r_mult *= nums[j]

        return [l*r for l, r in zip(left, right)]
    

    # Time complexity: O(n)
    # Space Complexity: O(n)